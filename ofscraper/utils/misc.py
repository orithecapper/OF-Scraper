import platform
import psutil
import asyncio
import logging
import ofscraper.utils.separate as seperate
import ofscraper.db.operations as operations
import ofscraper.utils.args as args_
import ofscraper.utils.downloadbatch as batchdownloader
import ofscraper.utils.download as download
import ofscraper.utils.config as config_


def getcpu_count():
    if platform.system() != 'Darwin':      
        return len(psutil.Process().cpu_affinity())
    else:
        return psutil.cpu_count()

def medialist_filter(medialist,model_id,username):
    log=logging.getLogger("shared")
    if not args_.getargs().dupe:
        media_ids = set(operations.get_media_ids(model_id,username))
        log.debug(f"Number of unique media ids in database for {username}: {len(media_ids)}")
        medialist = seperate.separate_by_id(medialist, media_ids)
        log.debug(f"Number of new mediaids with dupe ids removed: {len(medialist)}")  
        medialist=seperate.seperate_avatars(medialist)
        log.debug(f"Removed previously downloaded avatar/headers")
        log.debug(f"Final Number of media to download {len(medialist)}")

    else:
        log.info(f"forcing all downloads media count {len(medialist)}")
    return medialist


def download_picker(username, model_id, medialist):
    medialist=medialist_filter(medialist,model_id,username)
    if len(medialist)==0:
        return
    elif len(medialist)>=config_.get_download_semaphores(config_.read_config()) and getcpu_count()>1 and (args_.getargs().threads or config_.get_threads(config_.read_config()))>0:
        batchdownloader.process_dicts(username, model_id, medialist)
    else:
        asyncio.run(download.process_dicts(
                    username,
                    model_id,
                    medialist
                    ))
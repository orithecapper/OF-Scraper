A fork of onlyfans-scraper. It has been optimized to make it more feature complete with dc's onlyfans script.
A matter of fact with the right settings transitioning between the two scripts should be a easy enough process

In addition there are numerous filtering features to control exactly which type of content you want to scrape.
https://github.com/datawhores/ofscraper/blob/main/CHANGES.md

<h3>DISCLAIMERS:</h3>
<ol>
    <li>
        This tool is not affiliated, associated, or partnered with OnlyFans in any way. We are not authorized, endorsed, or sponsored by OnlyFans. All OnlyFans trademarks remain the property of Fenix International Limited.
    </li>
    <li>
        This is a theoritical program only and is for educational purposes. If you choose to use it then it may or may not work. You solely accept full responsability and indemnify the creator, hostors, contributors and all other involved persons from any any all responsability.
    </li>

 ## 1.8x Changes:
 - sync keys names across config(old keys will still work)
  * change username to model_username in metadata
  * change site_name to sitename in metadata
 - remove --purchased args
 - add purchase and pinned as post types
 - add letter-count argument
   * This is for counting letters and not words for
   textlength
 - added testing 
    * to install run poetry install --with test 
    * run with poetry run pytest
 - print path for each file
 - responsetype mapping in config
    * This is for example keeping all messages or paid post in same folder, but also allow long time users to keep their current structure
 - added a Post class to serve as a 'single source of truth' for all responsetypes
 - removed unused functions like download_paid that are no longer needed
 - prompts and config functions have been revamped
 - fixed bugs caused by duplicate uploads on pages
 - additional bugs and fixes

  ## Description:
  command-line program to download media, and to process other batch operations such as liking and unliking posts.
    

![CopyQ nsUBdI](https://user-images.githubusercontent.com/67020411/227816586-fb685959-cd3f-45af-adea-14773b7154f9.png)



## Installation

### Recommended python3.9 or python3.10


# Windows: 
```
pip install ofscraper
```
or 

```
pip install git+https://github.com/datawhores/ofscraper.git 
```

#  macOS/Linux
```
pip3 install ofscraper
```
or
```
pip3 install git+https://github.com/datawhores/ofscraper.git 
```

## Authentication

You'll need to retrive your auth information 
    
https://github.com/datawhores/ofscraper/wiki/Auth



# Usage

Whenever you want to run the program, all you need to do is type `ofscraper` in your terminal:

Basic usage is just to run the command below

```
ofscraper
```

![image](https://user-images.githubusercontent.com/67020411/230732583-dd064665-a59e-4714-92e7-393893061ac0.png)
  
 Select "Download content from a user" is all your need to get started with downloading content
 
## Liking/Unliking

It is also possible to batch unlike or like post by choosing the appropriate option in the menu
Note their are limitations (currently 1000) on how many post you can like per day

![image](https://user-images.githubusercontent.com/67020411/230735256-2d8aa788-53dc-49ee-ada8-5ddf5546851c.png)

## Selecting specific users

The fuzzy search system can be a little confusing see
    
https://github.com/datawhores/ofscraper/wiki/Fuzzy-Search 
    
## Other menu options    
  
 See: https://github.com/datawhores/ofscraper/wiki/Menu-Options 
 
 # commandline
 While the menu is easy to use, and convient. You may want more automation.
 
 The best way to do this is through the commandline system. This will allow you to skip the menu, and for example scrape a provided list of accounts
 
  https://github.com/datawhores/ofscraper/wiki/command-line-args
 
 # Customazation
    
https://github.com/datawhores/ofscraper/wiki/Customizing-save-path
https://github.com/datawhores/ofscraper/wiki/Config-Options

  
# Issues
Open a issue in this repo, or you can mention your issue in the discord

https://discord.gg/wN7uxEVHRK
    
    
## Common
### Status Down
      
This typically means that your auth information is not correct, or onlyfans signed you out.
### 404 Issue 
    
This could mean that the content you are trying to scrape is no longer present. It can also indicate that model has deleted her account, and it is no longer accesible on the platform
    
 ### Request taking a long time
   If a request fails ofscraper will pause and try again a few times. This can lead to certain runs taking longer and points.

 ## Known Limitations
 - 1000 likes is the max per day
    
    

# Migrating from DC script

You will need to change the settings so that the metadata option is compatible with your current folders
Additionally you might want to set the save_path, dir_path, and filename so they output similar outputs

The metadata path from dc's script is used for duplicate check so as long as your set the right path.
Files won't download a second time

https://github.com/datawhores/ofscraper/wiki/Migrating-from-DC-script
https://github.com/datawhores/ofscraper/wiki/Config-Options
https://github.com/datawhores/ofscraper/wiki/Customizing-save-path

Ask in the discord or open an issue if you need help with what to change to accomplish this



# Discord

https://discord.gg/wN7uxEVHRK
    
# Support
buymeacoffee.com/datawhores
    
BTC: bc1qcnnetrgmtr86rmqvukl2e24f5upghpcsqqsy87
    
ETH: 0x1d427a6E336edF6D95e589C16cb740A1372F6609


[![codecov](https://codecov.io/github/datawhores/ofscraper/branch/main/graph/badge.svg?token=U1F1PQ7LGM)](https://codecov.io/github/datawhores/ofscraper)










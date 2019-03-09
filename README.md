# jo-www

This is my personal webpage hosted on sunhwanj.heroku.com

## Buildpack

I'm using gitsubmodule to load publications and blog entries. To have submodule to work with heroku while use github as a backend, I used third party build pack. 

    heroku buildpacks:add --index 1 https://github.com/SectorLabs/heroku-buildpack-git-submodule.git 
    heroku config:set GIT_REPO_URL=git@github.com:sunhwan/jo-www.git

See https://github.com/SectorLabs/heroku-buildpack-git-submodule for more information.

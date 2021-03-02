
# Azure App Services

  

This application will run inside [Azure Web App Services](https://azure.microsoft.com/en-us/services/app-service/web/) and pull data from following two url's and expose an end point for Frontend data manipulation work.

  

- https://api.mentimeter.com/questions/48d75c359ce4

- https://api.mentimeter.com/questions/48d75c359ce4/result

  

## Prerequisites

  

-  [Azure](https://azure.microsoft.com/en-us/) account created to create Web App Services

  
  

## Installation

  
### Azure Web Services Backend
1.  Clone repository and move to directory backend
   `cd backend`
2.  Initialize a new git repository
	`git init`
3. Add Changes to repository
	`git add .`
 4. Commit the changes to the repository
	`git commit -m "Init C"`
5. Refer [URL](https://github.com/uglide/azure-content/blob/master/includes/publishing-with-git.md#enable-the-web-app-repository) and create an App service with Python 3.7. 
6. Add remote remote reference listed in Git URL
	`
git remote add azure https://username@needsmoregit.scm.azurewebsites.net:443/NeedsMoreGit.git
`

7. Once that's completed then push the code inside BackEnd to Azure.
`git push azure master`

### Azure Web Services Frontend
1. Refer [URL](https://github.com/uglide/azure-content/blob/master/includes/publishing-with-git.md#enable-the-web-app-repository) and create an App service with PHP
2. Add Changes to repository
	`git add .`
3.  Commit the changes to the repository
	`git commit -m "Init C"`

4.  Once that's completed then push the code inside BackEnd to Azure.
`git push azure master`

  
  

> https://phpflask.azurewebsites.net

> https://pyflask2.azurewebsites.net/voting?questionid=48d75c359ce4
# Azure App Services

This application will run inside [Azure Web App Services](https://azure.microsoft.com/en-us/services/app-service/web/) and pull data from following two url's and expose an end point for Frontend data manipulation work. 

- https://api.mentimeter.com/questions/48d75c359ce4
- https://api.mentimeter.com/questions/48d75c359ce4/result

## Prerequisites

- [Azure](https://azure.microsoft.com/en-us/) account created to create Web App Services 


## Installation

1.    Refer [URL](https://github.com/uglide/azure-content/blob/master/includes/publishing-with-git.md)  and create a App service with Python 3.7 support and push local git repository to Azure. 
2. Once that's completed then push the code inside BackEnd to Azure. 
3. Create a another app service  with PHP support and push the code inside FrontEnd to Azure.







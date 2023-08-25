# Introduction 
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 

# Getting Started

Installation:
- type "pip install ."  to install all required packages. 
- Copy files from  this [link](https://bechtle365.sharepoint.com/sites/BG365-Artificial-TheIntelligents/Freigegebene%20Dokumente/Forms/AllItems.aspx?csf=1&web=1&e=SOjgpo&xsdata=MDV8MDF8fDllM2U2YTIwZjM1OTQ4MzhkYzc2MDhkYmEyNGU1Nzk0fGVjZDEwNmRiOTA1ZTQyOGJhNTk2YTM1YTM2ZDA3YmIwfDB8MHw2MzgyODIyMjk1NjM1Nzk1MTB8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPakkxTW1SalpqRmhMVEkxWXpNdE5EYzJZUzFoTVRRMkxUazBNakl6TWpZME5ERmtabDg1T1RObVlUYzJNUzFqT0dFMExUUTNNbVl0T0RZNE55MHdPVGd5T0dSaU5qRTROekJBZFc1eExtZGliQzV6Y0dGalpYTXZiV1Z6YzJGblpYTXZNVFk1TWpZeU5qRTFOVGsyT1E9PXwxODYzNzM2YzJjOTc0MzE1ZGM3NjA4ZGJhMjRlNTc5NHw1ZTFkMzMyMTZlMzc0NGFlYmJmZGZiNTA5YjRhMjk4NA%3D%3D&sdata=YTJmNS9PdHZQeGo3N3gwVjdEYzBkSEI4SHNXNTJrTDg3UlBuOEo3WE9JQT0%3D&ovuser=ecd106db%2D905e%2D428b%2Da596%2Da35a36d07bb0%2Candreas%2Eboettcher%40bechtle%2Ecom&OR=Teams%2DHL&CT=1692626239342&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzA3MDMwNzM0NiIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&cid=8a5bb202%2D6f89%2D42ab%2Da8bc%2D0e0ff48397e4&FolderCTID=0x0120000E867F22DDD9314FA2C7D6D0D2F51BBC&id=%2Fsites%2FBG365%2DArtificial%2DTheIntelligents%2FFreigegebene%20Dokumente%2FGeneral%2FMVP&viewid=d5c0c247%2Dc2da%2D480c%2D949e%2Dfcfbbdbfe1fd) to data/

Usage:
- start uvicorn server with uvicorn main:app --reload (reload makes the server reload everytime you save)
- use "python send_request.py" to send a test request.


# Build and Test
- add new functions/classes to src/routing_service/ (develop in notebooks/)
- add tests in tests/
- run tests with "python -m unittest



# Contribute

- This needs to be reviewed by Patrick and/or the recommendend best practises need to be checked.
Current Form of developing:
- create a feature branch (git checkout -b feature_1)
- finish feature, commit it on this branch (git add, git commit -m 'finished feature 1')
- checkout develop branch, fetch and pull from remote 
- checkout feature branch and merge develop  (git merge develop)
- push the branch (git push -u origin feature_1)
- create a pull request on devops to merge feature_1 into develop. add reviewer(s) and a work item
- when pull request is done, you can delete the feature branch
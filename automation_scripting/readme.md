### Archived results
Original results are archived in ```~/archived``` folder. **Do not** run ```info_extractor.py``` in this folder. This folder is for archiving results only.

### Setting up
```
## once in ~/automation_scripting create a python3 virtual environment
pip3 install virtualenv
virtualenv <env>

## activate environment and install required libraries
activate <env>/bin/activate
pip3 install -r requirements.txt
```

### Re-creating results
```
python3 info_extractor.py <URL>
```
URL defaults to given URL in the exercise. An error might be thrown during the domain-name resolving process, as the free-version of dnsdumpster is used.
IF this happens, or if ```Resolved IP addresses.csv``` end up blank, copy over ```archived/Resolved IP addresses.csv```

## UArizona Python Grouper Example

### Installation

- Install dependencies. In project directory run:
 ```
 python3 -m pip install -r requirements.txt -t .
 ```
- Set EDS username and password in `.env` file. EDS account access can be requested at [https://apps.iam.arizona.edu/](https://apps.iam.arizona.edu/).
- Grant your EDS user `UPDATE` access to the Grouper group(s) you wish to add/delete users to/from. You can do this in the [Grouper UI](https://grouper.iam.arizona.edu/) via the "Privileges" tab on the respective groups.

### Running
```
python3 ./test.py <ADD|DEL> <netid> <group>
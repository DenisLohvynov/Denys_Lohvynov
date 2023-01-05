To install some requirements run in the folder of the project the following command: 
```bash
pip install -r requirements.txt
```
you need to have FireFox and plugin for Selenium additionaly.

To run the program just run the command

```
behave
```

in your terminal. If there's a problem you should expicitly add the location of your Firefox and plugin for Firefox as such

```bash
behave -D location="FireFox_location|Driver_location"
```

To get a teport out of the program you need to run
```bash
behave -D location="FireFox_location|Driver_location" -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
```
or just
```bash
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
```


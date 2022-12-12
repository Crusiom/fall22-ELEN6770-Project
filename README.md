# fall22-ELEN6770-Project

**Danling Wei & Xuechen Zhou**



### FrontEnd

The front end Vue.js code is in frontEnd folder. It is implemented by Vue-CLI in Node.js. If you want to test it. Make sure Node.js and Vue-CLI is installed.



### BackEnd

The back end Lambda function is in backEnd folder. Provided that each Lambda function is corresponding to a lambda_fucntion.py. I set the name of file lambda function LAMBDA_NAME.py. But the actual structure in Lambda is below:

**Lambda Functions**

- Message

  - lambda_function.py

    - ```python
      import boto3
      import json
      ...
      ```

      

- Send

  ...
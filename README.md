## Environment Setting

1. Use CMD
2. Import requirements.txt
3. Create virtual env
   * cd to current directory
   * enter 
    ```
    > virtualenv venv
    > .\venv\Scripts\activate.bat
    ```
4. Set Flask 
    ```
    > set FLASK_APP=server.py
    > set FLASK_ENV=development
    ```
5. Create DB
   ```
    > flask db init
    > flask db migrate
    > flask initdb
    > flask forge
    > flask run -h 140.xxx.xx.xx -p xxxx
   ```

6. Test Backend API service
   * Use Daimler_Based Distributed Mobility Service Internal API Document_v5.md

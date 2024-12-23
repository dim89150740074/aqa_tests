import time

import pytest


class TestExample:
    @pytest.mark.skip
    def test_check_connection(self, db_con):
        cursor = db_con.cursor()
        cursor.execute("SELECT * FROM employees")
        print(cursor.fetchone())

    # @pytest.mark.skip
    def test_login(self, generate_data):
        login, password = generate_data
        print(login, password)

    @pytest.mark.skip
    def test_login2(self, generate_data2):
        login = generate_data2.login
        password = generate_data2.password
        print(login, password)

    @pytest.mark.skip
    def test_login3(self, generate_data3):
        login = generate_data3.login
        password = generate_data3.password
        print(login, password)

    @pytest.mark.skip
    @pytest.mark.usefixtures("generate_data4")
    def test_login4(self):
        login = self.login
        password = self.password
        print(login, password)

    @pytest.mark.skip
    @pytest.mark.usefixtures("db_connection2")
    def test_check_connection2(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employees")
        print(cursor.fetchall())
        self.connection.close()

    @pytest.mark.skip
    @pytest.mark.usefixtures("db_conn3")
    def test_check_connection2(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employees")
        print(cursor.fetchone())

    # @pytest.mark.skip
    @pytest.mark.usefixtures("browser")
    def test_open_browser(self):
        url = "https://demoqa.com/select-menu"
        self.driver.get(url)
        time.sleep(5)
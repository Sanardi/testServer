import json
import time
import requests
import dbcon



class testServer:
    '''
    This Class lets you make requests to your chosen website and sends the stauts codes
    into Postgresql. The default waiting
    time between requests in 30 seconds.
    This can be overriden by passing waiting_time = <WHATEVER_in_seconds> when initializing the class
    '''

    def __init__(self, url = "https://datanalysis.ai", topic = "checking_website_availability", waiting_time = 30, table_name = "serverdata"):

        self.url = url
        self.waiting_time = waiting_time
        self.topic = topic
        self.tableName = table_name

    def make_request(self):
        status_data = {}
        try:
            #acessing the website:'
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
            headers={'User-Agent':user_agent}
            r = requests.get(self.url, headers = headers)
            status_data["time"] = time.time()
            status_data["code"] = r.status_code
            status_data["response_time"] = r.elapsed.total_seconds()

            return status_data

        except Exception as e:
            print(e)


    def _write_DB(self):
        test_server_responses = self.make_request()

        columns = ', '.join("`" + str(x).replace('*', '_') + "`" for x in test_server_responses.keys())
        values = ', '.join("'" + str(x).replace('*', '_') + "'" for x in test_server_responses.values())
        sql = "INSERT INTO `%s` ( %s ) VALUES ( %s );" % (table_name, columns, values)
        print(sql)
        conn = dbcon.make_con(sql)

            time.sleep(self.waiting_time)

    def run(self):
        print("I will now check the status codes and send them to Postgresql")
        while True:
            self._write_DB()

if __name__ == '__main__':
    bla = testServer()
    bla.run()

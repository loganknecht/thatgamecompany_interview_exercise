# Python Standard Libraries
import json
import random
# Third-Party Libraries
from locust import HttpLocust, TaskSet, task
# Custom Libraries
# N/A


def create_user():
    """TODO."""
    i = 0
    while True:
        new_user = {
            "username": "test{}".format(i),
            "password": "test_password",
            "email": "test{}@test.com".format(i),
        }
        i = i + 1
        yield new_user

users = create_user()


def print_response(response):
    """TODO."""
    print("=" * 80)
    print("response_content: {}".format(response.content))
    print("response_status_code: {}".format(response.status_code))


class UserBehavior(TaskSet):

    def on_start(self):
        """on_start is called when a Locust start before any task is scheduled

        Used to generate user specific credentials for testing.
        """
        # TODO: do the opposite of pop here, cut?
        new_user = next(users)

        self.user_data = new_user
        self.signup()
        # self.login()

    def signup(self):
        response = self.client.post("/api/v1/signup/",
                                    self.user_data)
        response_content = response.content

        if isinstance(response_content, bytes):
            # Assumes response is always a byte object
            response_content_string = response_content.decode()
            json_data = json.loads(response_content_string)

            self.user_id = json_data["user"]["id"]
            self.token = json_data["user"]["token"]
        else:
            self.token = ""

    # @task(1)
    # def login(self):
    #     if(self.token is None or
    #             self.token == ""):
    #         response = self.client.post("/api/v1/login/",
    #                                     auth=(self.user_data["username"],
    #                                           self.user_data["password"],))
    #         response_content = response.content

    #         if isinstance(response_content, bytes):
    #             # Assumes response is always a byte object
    #             response_content_string = response_content.decode()
    #             json_data = json.loads(response_content_string)

    #             if "token" in json_data:
    #                 self.token = json_data["token"]

    @task(1)
    def api_documentation(self):
        self.client.get("/api/v1/")

    @task(1)
    def ping_endpoint(self):
        self.client.get("/api/v1/ping/")

    @task(5)
    def dig_endpoint(self):
        if(self.token is not None and
                self.token != ""):
            amount_to_dig = random.randint(1, 100)
            header_authorization = "Bearer {}".format(self.token)
            header_content_type = "application/json"
            headers = {
                "Content-Type": header_content_type,
                "Authorization": header_authorization,
            }
            data = {
                "amount_to_dig": amount_to_dig,
            }

            response = self.client.post("/api/v1/dig/",
                                        data=json.dumps(data),
                                        headers=headers)
            # print_response(response)

    @task(3)
    def purchase_endpoint(self):
        if(self.token is not None and
                self.token != "" and
                self.user_id is not None and
                self.user_id != ""):

            item_to_purchase = random.randint(1, 3)
            user_to_give_to = random.randint(0, 998)

            header_authorization = "Bearer {}".format(self.token)
            header_content_type = "application/json"

            headers = {
                "Content-Type": header_content_type,
                "Authorization": header_authorization,
            }
            data = {
                "purchaser_id": self.user_id,
                "recipient_id": item_to_purchase,
                "item_id": item_to_purchase,
            }

            response = self.client.post("/api/v1/shop/purchase/",
                                        data=json.dumps(data),
                                        headers=headers)
            # print_response(response)


class LoadTesting(TaskSet):
    tasks = {
        UserBehavior: 1,
    }


class ApiUser(HttpLocust):
    task_set = LoadTesting
    min_wait = 1000
    max_wait = 5000

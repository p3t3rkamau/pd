from flask import Flask, request
import requests
import base64

app = Flask(__name__)

# URL of the file you want to write to
url = "https://api.github.com/repos/p3t3rkamau/pd/contents/contents/form_data.csv"

# Headers for the request
headers = {
    "Authorization": "Bearer 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",
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/json"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Data you want to write to the file
        data_to_write = f"{request.form['first_name']},{request.form['last_name']},{request.form['email']},{request.form['phone_number']},{request.form['password']}\n"

        # Making a GET request to fetch the current contents of the file
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            file_contents = base64.b64decode(data["content"]).decode('utf-8')
            # Appending the new data to the file contents
            file_contents += data_to_write
            # Encoding the data in base64
            encoded_data = base64.b64encode(file_contents.encode()).decode('utf-8')
            sha = data["sha"]

            # Data for the request body
            data = {
                "message": "Adding form data",
                "content": encoded_data,
                "sha": sha
            }

            # Making the PUT request to update the file
            response = requests.put(url, headers=headers, json=data)
            if response.status_code == 200:
                return "Data written successfully"
            else:
                return f"Failed to write data. Response: {response.text}"
        else:
            return f"Failed to fetch file contents. Response: {response.text}"
    return """
    <style>
  form {
    width: 500px;
    margin: 50px auto;
    padding: 30px;
    background-color: #f2f2f2;
    border: 1px solid #ccc;
    border-radius: 10px;
  }

  label {
    font-weight: bold;
    margin-top: 10px;
    display: block;
  }

  input[type="text"], input[type="email"] {
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    font-size: 16px;
  }

  input[type="submit"] {
    width: 100%;
    padding: 10px;
    margin-top: 20px;
    border-radius: 5px;
    border: none;
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    cursor: pointer;
  }

  input[type="submit"]:hover {
    background-color: #3e8e41;
  }
</style>
       <form method="post">
        First Name: <input type="text" name="first_name"><br>
        Last Name: <input type="text" name="last_name"><br>
        Email: <input type="email" name="email"><br>
        Phone Number: <input type="tel" name="phone_number"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Submit">
        </form>

    """

if __name__ == "__main__":
    app.run()

# import requests
# import base64

# # URL of the file you want to write to
# url = "https://api.github.com/repos/p3t3rkamau/pd/contents/contents/form_data.csv"

# # Data you want to write to the file
# data_to_write = "peter,petercubolt@gmail.com"

# # Encoding the data in base64
# encoded_data = base64.b64encode(data_to_write.encode()).decode('utf-8')

# # Headers for the request
# headers = {
#     "Authorization": "Bearer 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",
#     "Accept": "application/vnd.github+json",
#     "Content-Type": "application/json"
# }

# # Data for the request body

# data = {
#     "message": "Adding form data",
#     "content": encoded_data,
# }

# # Making the PUT request to update the file
# response = requests.put(url, headers=headers, json=data)

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     data = response.json()
#     sha = data["sha"]
#     data = {
#         "message": "Adding form data",
#         "content": encoded_data,
#         "sha": sha
#     }
#     response = requests.put(url, headers=headers, json=data)
#     if response.status_code == 200:
#         print("Data written successfully")
#     else:
#         print(f"Failed to write data. Response: {response.text}")
# else:
#     print(f"Failed to fetch file contents. Response: {response.text}")



# Checking if the request was successful
# if response.status_code == 200:
#     print("Data written successfully")
# else:
#     print(f"Failed to write data. Response: {response.text}")


# from flask import Flask, request
# import csv
# import requests

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
        
#         # store data in a list
#         data = [name, email]
        
#         # write data to a local CSV file
#         with open('form_data.csv', 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(data)


#         base_url = 'https://api.github.com'
#         username = 'p3t3rkamau'
#         repo = 'pd'

#         headers = {
#             'Authorization': 'token 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',
#             'Content-Type': 'application/json'
#         }

#         data = [name, email]
#         endpoint = '/repos/{}/{}/contents/contents/form_data.csv'.format(username, repo)
#         encoded_data = ','.join(data).encode('utf-8')
#         print(encoded_data)
#         response = requests.put(base_url + endpoint, headers=headers, data=encoded_data)
#         print(response)

#         if response.status_code == 200:
#             print('Data written successfully to form_data.csv')
#         else:
#             print('Failed to write data to form_data.csv. Response code: {}'.format(response.status_code))

        
        
#     return '''
#         <form action="/" method="post">
#           <label for="name">Name:</label>
#           <input type="text" id="name" name="name">

#           <label for="email">Email:</label>
#           <input type="email" id="email" name="email">

#           <input type="submit" value="Submit">
#         </form>
#     '''

# if __name__ == '__main__':
#     app.run(debug=True)

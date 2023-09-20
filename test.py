
import pandas as pd
import re
import collections

txt = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dummy Contact Information</title>
</head>
<body>
<h1>Contact List</h1>
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Job Title</th>
      <th>Responsibilities</th>
      <th>Phone Number</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John Doe</td>
      <td>Software Engineer</td>
      <td>Develop and maintain software applications</td>
      <td>(123) 456-7890</td>
      <td>john@example.com</td>
    </tr>
    <tr>
      <td>Jane Smith</td>
      <td>Marketing Specialist</td>
      <td>Create marketing campaigns and analyze results</td>
      <td>(234) 567-8901</td>
      <td>jane@example.com</td>
    </tr>
    <tr>
      <td>Michael Johnson</td>
      <td>Accountant</td>
      <td>Manage financial records and prepare reports</td>
      <td>(345) 678-9012</td>
      <td>michael@example.com</td>
    </tr>
    <tr>
      <td>Susan Williams</td>
      <td>Project Manager</td>
      <td>Plan, execute, and monitor project activities</td>
      <td>(456) 789-0123</td>
      <td>susan@example.com</td>
    </tr>
    <tr>
      <td>David Lee</td>
      <td>Graphic Designer</td>
      <td>Create visual content for marketing materials</td>
      <td>(567) 890-1234</td>
      <td>david@example.com</td>
    </tr>
    <tr>
      <td>Emily Davis</td>
      <td>HR Manager</td>
      <td>Manage human resources functions</td>
      <td>(678) 901-2345</td>
      <td>emily@example.com</td>
    </tr>
    <tr>
      <td>Robert Brown</td>
      <td>Sales Representative</td>
      <td>Generate leads and close sales</td>
      <td>(789) 012-3456</td>
      <td>robert@example.com</td>
    </tr>
    <tr>
      <td>Linda Miller</td>
      <td>Customer Support Specialist</td>
      <td>Assist customers with inquiries and issues</td>
      <td>(890) 123-4567</td>
      <td>linda@example.com</td>
    </tr>
    <tr>
      <td>James Wilson</td>
      <td>Operations Manager</td>
      <td>Oversee daily business operations</td>
      <td>(901) 234-5678</td>
      <td>james@example.com</td>
    </tr>
    <tr>
      <td>Sarah Taylor</td>
      <td>Content Writer</td>
      <td>Create written content for various platforms</td>
      <td>(012) 345-6789</td>
      <td>sarah@example.com</td>
    </tr>
  </tbody>
</table>
</body>
</html>"""

print("####Extracting Contact Information from a Web Page using Python and Regular Expressions###")
print()
#Extracting the data
email_r = re.findall(r"\w*@\w*\.\w*", txt, re.I)

phone_num = re.findall(r"\(\d{3}\)\s\d{3}-\d{4}", txt, re.I)

name = re.findall(r"\b[A-Z]\w*\b\s\b[A-Z]\w*\b", txt)

name_remove = [0, 1, 2, 3, 5, 7, 10, 12, 14, 16, 18, 20, 22]

for index in sorted(name_remove, reverse=True):
    del name[index]


#Converting to series
email_s = pd.Series(email_r)
phone_num_s = pd.Series(phone_num)
name_s = pd.Series(name)


#Final dataframe
print("###DataFrame###")
Dataframe = pd.DataFrame({ "Name": name_s,
    "Phone": phone_num_s,
    "Email": email_s})

print(Dataframe)

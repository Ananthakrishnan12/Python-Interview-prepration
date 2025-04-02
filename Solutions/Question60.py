string_methods_data = {
    'Email': ['alice@example.com', 'bob.smith@test.co.uk', 'charlie123@domain.net', 'david_jones@mail.org', 'eve.green@sample.io', 'frank.white@web.com', 'grace.black@data.gov', 'hannah.brown@code.ai', 'ivy.gray@info.edu', 'jack.king@network.biz'],
    'Name': ['Alice Smith', 'Bob Smith', 'Charlie Brown', 'David Jones', 'Eve Green', 'Frank White', 'Grace Black', 'Hannah Brown', 'Ivy Gray', 'Jack King'],
    'Address': ['123 Main St', '456 Oak Ave', '789 Pine Ln', '101 Elm Rd', '202 Maple Dr', '303 Birch Ct', '404 Cedar Pl', '505 Willow Way', '606 Aspen Blvd', '707 Redwood St']
}

import pandas as pd

df=pd.DataFrame(string_methods_data)
df["Domain"]=df["Email"].str.split("@").str[1]
print(df["Domain"])

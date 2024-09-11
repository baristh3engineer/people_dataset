from names import names

from descriptions import descriptions

if len(names) == len(descriptions):
    print("Lengths match:", len(names))
else:
    print(f"Lengths mismatch: {len(names)} names, {len(descriptions)} descriptions")

import pandas as pd

data = {
    'Name': names,
    'Description': descriptions
}

df = pd.DataFrame(data)
df.to_csv('people.csv', index=False)

print("CSV file created successfully.")
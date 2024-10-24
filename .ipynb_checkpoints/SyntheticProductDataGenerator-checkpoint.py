#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from faker import Faker
import random

class SyntheticProductDataGenerator:
    def __init__(self, num_products=1000):
        self.num_products = num_products
        self.fake = Faker()
        
        self.categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports & Outdoors', 'Books', 'Toys & Games']
        self.brands = ['TechPro', 'FashionStyle', 'HomeComfort', 'SportsMaster', 'BookWorm', 'PlayFun']
        
    def generate_product_id(self):
        return f'P{self.fake.unique.random_number(digits=4)}'
    
    def generate_product_name(self, category):
        adjectives = ['Amazing', 'Incredible', 'Fantastic', 'Awesome', 'Ultimate', 'Premium']
        if category == 'Electronics':
            nouns = ['Smartphone', 'Laptop', 'Headphones', 'Smartwatch', 'Camera', 'Tablet']
        elif category == 'Clothing':
            nouns = ['T-shirt', 'Jeans', 'Dress', 'Jacket', 'Shoes', 'Hat']
        elif category == 'Home & Garden':
            nouns = ['Sofa', 'Lamp', 'Rug', 'Plant', 'Pillow', 'Vase']
        elif category == 'Sports & Outdoors':
            nouns = ['Bicycle', 'Tent', 'Backpack', 'Kayak', 'Yoga Mat', 'Running Shoes']
        elif category == 'Books':
            return f"The {self.fake.word().title()} {self.fake.word().title()}"
        else:  # Toys & Games
            nouns = ['Board Game', 'Puzzle', 'Action Figure', 'Doll', 'Building Blocks', 'Remote Control Car']
        
        return f"{random.choice(adjectives)} {random.choice(nouns)}"
    
    def generate_description(self, name, category):
        return f"A high-quality {category.lower()} product. This {name} is perfect for {self.fake.sentence(nb_words=6)}"
    
    def generate_price(self, category):
        if category == 'Electronics':
            return round(random.uniform(50, 2000), 2)
        elif category == 'Clothing':
            return round(random.uniform(10, 200), 2)
        elif category == 'Home & Garden':
            return round(random.uniform(20, 500), 2)
        elif category == 'Sports & Outdoors':
            return round(random.uniform(15, 1000), 2)
        elif category == 'Books':
            return round(random.uniform(5, 50), 2)
        else:  # Toys & Games
            return round(random.uniform(10, 100), 2)
    
    def generate_dataset(self):
        data = []
        for _ in range(self.num_products):
            category = random.choice(self.categories)
            name = self.generate_product_name(category)
            product = {
                'product_id': self.generate_product_id(),
                'name': name,
                'category': category,
                'brand': random.choice(self.brands),
                'description': self.generate_description(name, category),
                'price': self.generate_price(category),
                'rating': round(random.uniform(1, 5), 1),
                'num_reviews': random.randint(0, 1000)
            }
            data.append(product)
        
        return pd.DataFrame(data)

    def save_dataset(self, df, file_path):
        df.to_csv(file_path, index=False)
        print(f"Dataset saved to {file_path}")

# Usage example
generator = SyntheticProductDataGenerator(num_products=1000)
product_df = generator.generate_dataset()
generator.save_dataset(product_df, 'synthetic_products.csv')

# Display the first few rows of the dataset
print(product_df.head())

# Display summary statistics
print(product_df.describe())

# Display the distribution of products across categories
print(product_df['category'].value_counts(normalize=True))


# In[ ]:





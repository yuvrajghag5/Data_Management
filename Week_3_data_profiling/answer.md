-- Column analysis --

- The column orderID and CustomerID have many unique values
and the column OrderID can be used as identifier becaause 100% of the rows are unique 
representing a unique number for all the orders.
- The date, emails are valid but not in numeric data type.


-- Cleaning rules based on profiling --

- handling missing values depends upon the importance of the coulmn and its datatype. As present in the dataset the column 'Satisfaction_Score' has the data type numeric from 1-5 regarding the customer's satisfaction on the bases of the order, it also has some null value which cannot be replaced with 0 because that would mean the customer absolutely hated the order.

- The duplicate records from the orderID should be removed because it is the identifier and a single person can order multiple times that means the oderid will be unique evreytime but not the custormerID its details.

- invalid values like country, date, city , product category should be corrected but not removed. 



-- Decide the pipeline --

-In ETL (Extract → Transform → Load), data profiling happens during the Transformation stage before loading the data into the data warehouse/database.

-In ELT (Extract → Load → Transform), profiling happens after loading the raw data into the target system like data warehouse/database.

-ETL (Extract → Transform → Load) is a better approach for this dataset because it contains many quality issues like inconsistent text capitalization, duplicate rows, null values, mixed date formats, etc. 
cleaning before loading prevents bad data from entering the database.
the dataset is relatively samll , so ETL is simpler and more efficenet.


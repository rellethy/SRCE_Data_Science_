* Load the dataset
import delimited "/path/to/your/books_data.csv", clear

* Data cleaning commands here
* For example, converting string variables to numeric
destring first_published, replace

* Regression analysis
regress sales_in_millions first_published

* Generate plot
scatter sales_in_millions first_published || lfit sales_in_millions first_published


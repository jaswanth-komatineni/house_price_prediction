import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_pie_chart(file_path):

    hp = pd.read_csv(file_path)
    
    #Percentage distribution of source and destination
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    hp['NUM_OF_BATHROOMS'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Distribution of Bathrooms')
    # Create a pie chart for Category2
    plt.subplot(1, 2, 2)
    hp['NUM_OF_BEDROOMS'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Distribution of Bedrooms')
    plt.tight_layout()
 

    # Save the plot as an image file
    image_path = 'static/eda_result6.png'
    plt.savefig(image_path)
    plt.close()  # Close the plot to free up memory
    return image_path

if __name__ == "__main__":
    file_path = 'cleaned_housing_dataset.csv'
    image_path = generate_pie_chart(file_path)
    print(f"Image saved at: {image_path}")

#plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_pie_chart(file_path):

    hp = pd.read_csv(file_path)
    
    sns.jointplot(x='TOTAL_HOUSE_AREA_sqft', y='PRICE', data=hp, kind='scatter')
    plt.xlabel('tOTAL House Area (sqft)')
    plt.ylabel('Price')
    plt.title('Joint Plot of Living Area vs. Price')

    # Save the plot as an image file
    image_path = 'static/eda_result8.png'
    plt.savefig(image_path)
    plt.close()  # Close the plot to free up memory
    return image_path

if __name__ == "__main__":
    file_path = 'cleaned_housing_dataset.csv'
    image_path = generate_pie_chart(file_path)
    print(f"Image saved at: {image_path}")

#plt.show()
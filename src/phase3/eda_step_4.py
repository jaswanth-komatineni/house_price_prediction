
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_pie_chart(file_path):

    hp = pd.read_csv(file_path)
    
    import seaborn as sns

    # Plot box plot of a numerical feature
    sns.boxplot(x=hp['LIVING_AREA_sqft'], y=hp['PRICE'])
    plt.xlabel('LIVING_AREA_sqft')
    plt.ylabel('PRICE')
    plt.title('Box Plot of House Price Prediction')
 

    # Save the plot as an image file
    image_path = 'static/eda_result4.png'
    plt.savefig(image_path)
    plt.close()  # Close the plot to free up memory
    return image_path

if __name__ == "__main__":
    file_path = 'cleaned_housing_dataset.csv'
    image_path = generate_pie_chart(file_path)
    print(f"Image saved at: {image_path}")

#plt.show()
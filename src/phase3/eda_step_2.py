
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_pie_chart(file_path):

    hp = pd.read_csv(file_path)
    plt.figure(figsize=(10,7))
    sns.heatmap(hp.select_dtypes(include='number').drop(['YEAR_BUILT', 'YEAR_RENOVATED'], axis=1).corr(),annot=True);

    # Save the plot as an image file
    image_path = 'static/eda_result2.png'
    plt.savefig(image_path)
    plt.close()  # Close the plot to free up memory
    return image_path

if __name__ == "__main__":
    file_path = 'cleaned_housing_dataset.csv'
    image_path = generate_pie_chart(file_path)
    print(f"Image saved at: {image_path}")

#plt.show()
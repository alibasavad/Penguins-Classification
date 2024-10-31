from utils.Estimator import ML_Estimator, Variance_Squaremat
from utils.print_list import printList
from utils.PCA import Normalize_Data, PCA_Transform
from utils.save_figure import save, Save_Contour_Figure_3_Class
from utils.Classifier import MeanAccuracy
import utils.Data as Data


print(
    f"Species : {printList(Data.Species)} \nFeatures : {printList(Data.Features)} ")
print(f"Adelie lenght : {len(Data.Adelie_Data)}")
print(f"Chinstrap lenght : {len(Data.Chinstrap_Data)}")
print(f"Gentoo lenght : {len(Data.Gentoo_Data)}")

normalizeData = Normalize_Data(Data.All_Data, Data.Features)

Data_2D = PCA_Transform(normalizeData, Data.All_Data)

Data_2D_Unnormal = PCA_Transform(
    Data.All_Data.loc[:, Data.Features].values, Data.All_Data)

# unnormal data

Adelie = Data.Extract_Species_Values(Data_2D_Unnormal, "Adelie")
Chinstrap = Data.Extract_Species_Values(Data_2D_Unnormal, "Chinstrap")
Gentoo = Data.Extract_Species_Values(Data_2D_Unnormal, "Gentoo")


Adelie_Train, Adelie_Test = Data.Seperate_Test_Train(Adelie)
Chinstrap_Train, Chinstrap_Test = Data.Seperate_Test_Train(Chinstrap)
Gentoo_Train, Gentoo_Test = Data.Seperate_Test_Train(Gentoo)

Adelie_Train_Mean, Adelie_Train_Variance = ML_Estimator(Adelie_Train)
Gentoo_Train_Mean, Gentoo_Train_Variance = ML_Estimator(Gentoo_Train)
Chinstrap_Train_Mean, Chinstrap_Train_Variance = ML_Estimator(Chinstrap_Train)

Var_Adelie = Variance_Squaremat(Adelie_Train_Variance)
Var_Gentoo = Variance_Squaremat(Gentoo_Train_Variance)
Var_Chinstrap = Variance_Squaremat(Chinstrap_Train_Variance)


meanAccuracy = MeanAccuracy([Adelie_Test, Gentoo_Test, Chinstrap_Test], [
    Adelie_Train_Mean, Gentoo_Train_Mean, Chinstrap_Train_Mean], [Var_Adelie, Var_Gentoo, Var_Chinstrap])

print("Unnormal Data Accuracy : ", meanAccuracy)

# Save_Contour_Figure_3_Class([Adelie, Gentoo, Chinstrap], [Adelie_Train_Mean, Gentoo_Train_Mean, Chinstrap_Train_Mean], [
#                             Var_Adelie, Var_Gentoo, Var_Chinstrap], "2_Dimentional_Contour_Boundaries_Unnormal", "Principal 1", "Principal 2", "2_Dimentional_Contour_Boundaries_Unnormal")


# normal data

Adelie = Data.Extract_Species_Values(Data_2D, "Adelie")
Chinstrap = Data.Extract_Species_Values(Data_2D, "Chinstrap")
Gentoo = Data.Extract_Species_Values(Data_2D, "Gentoo")


Adelie_Train, Adelie_Test = Data.Seperate_Test_Train(Adelie)
Chinstrap_Train, Chinstrap_Test = Data.Seperate_Test_Train(Chinstrap)
Gentoo_Train, Gentoo_Test = Data.Seperate_Test_Train(Gentoo)

Adelie_Train_Mean, Adelie_Train_Variance = ML_Estimator(Adelie_Train)
Gentoo_Train_Mean, Gentoo_Train_Variance = ML_Estimator(Gentoo_Train)
Chinstrap_Train_Mean, Chinstrap_Train_Variance = ML_Estimator(Chinstrap_Train)

Var_Adelie = Variance_Squaremat(Adelie_Train_Variance)
Var_Gentoo = Variance_Squaremat(Gentoo_Train_Variance)
Var_Chinstrap = Variance_Squaremat(Chinstrap_Train_Variance)

meanAccuracy = MeanAccuracy([Adelie_Test, Gentoo_Test, Chinstrap_Test], [
    Adelie_Train_Mean, Gentoo_Train_Mean, Chinstrap_Train_Mean], [Var_Adelie, Var_Gentoo, Var_Chinstrap])

print("Normal Data Accuracy : ", meanAccuracy)

# Save_Contour_Figure_3_Class([Adelie, Gentoo, Chinstrap], [Adelie_Train_Mean, Gentoo_Train_Mean, Chinstrap_Train_Mean], [
#                             Var_Adelie, Var_Gentoo, Var_Chinstrap],  "2_Dimentional_Contour_Boundaries_Normal", "Principal 1", "Principal 2", "2_Dimentional_Contour_Boundaries_Normal")


# save(Data_2D, Data_2D_Unnormal)

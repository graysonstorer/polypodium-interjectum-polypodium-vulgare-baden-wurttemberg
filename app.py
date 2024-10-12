import csv
import numpy as np

#leaf data
leaf_lengths_vulgare = []
leaf_lengths_interjectum = []
leaf_widths_vulgare = []
leaf_widths_interjectum = []

#spore data
spore_widths_interjectum = []
spore_widths_vulgare = []
spore_lengths_interjectum = []
spore_lengths_vulgare = []

#sporangia cell data
sporangia_annulus_cell_count_interjectum = []
sporangia_annulus_cell_count_vulgare = []
sporangia_basal_cell_count_interjectum = []
sporangia_basal_cell_count_vulgare = []

def collectData():
    with open('data/leaf_length_measurements.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if (row[0] == 'P. vulgare'):
                if (float(row[1]) != -1) & (float(row[2]) != -1):
                    leaf_lengths_vulgare.append(float(row[1]))
                    leaf_widths_vulgare.append(float(row[2]))
            if (row[0] == 'P. interjectum'):
                if (float(row[1]) != -1) & (float(row[2]) != -1):
                    leaf_lengths_interjectum.append(float(row[1]))
                    leaf_widths_interjectum.append(float(row[2]))
    with open('data/spore_data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if (row[0] == 'P. vulgare'):
                if (float(row[1]) != -1) & (float(row[2]) != -1):
                    spore_lengths_vulgare.append(float(row[1]))
                    spore_widths_vulgare.append(float(row[2]))
            if (row[0] == 'P. interjectum'):
                if (float(row[1]) != -1) & (float(row[2]) != -1):
                    spore_lengths_interjectum.append(float(row[1]))
                    spore_widths_interjectum.append(float(row[2]))
    with open('data/annulus_and_basel_cell_measurement.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if (row[0] == 'P. vulgare'):
                if (float(row[1]) != -1) & (float(row[2]) != -1):
                    sporangia_annulus_cell_count_vulgare.append(float(row[1]))
                    sporangia_basal_cell_count_vulgare.append(float(row[2]))
            elif (row[0] == 'P. interjectum'):
                if (float(row[1]) != -1) & (float(row[2]) != -1):
                    sporangia_annulus_cell_count_interjectum.append(float(row[1]))
                    sporangia_basal_cell_count_interjectum.append(float(row[2]))

def mean(array):
    sum = 0.0
    number = 0.0
    for i in range(len(array)):
        sum += float(array[i])
        number += 1.0
    if (number == 0) | (number == 0):
        return 0.0
    return float(sum / number)

collectData()
print("DATA REGARDING P. VULGARE\n")
print("Mean leaf lengths of P. vulgare: ", mean(leaf_lengths_vulgare))
print("Mean leaf widths of P. vulgare: ", mean(leaf_widths_vulgare))
print("Mean spore lengths of P. vulgare: ", mean(spore_lengths_vulgare))
print("Mean spore widths of P. vulgare: ", mean(spore_widths_vulgare))
print("Mean basal cell count of sporangia in P. vulgare: ", mean(sporangia_basal_cell_count_vulgare))
print("Mean annulus cell count of sporangia in P. vulgare: ", mean(sporangia_annulus_cell_count_vulgare), "\n")
print("DATA REGARDING P. INTERJECTUM \n")
print("Mean leaf lengths of P. interjectum: ", mean(leaf_lengths_interjectum))
print("Mean leaf widths of P. interjectum: ", mean(leaf_widths_interjectum))
print("Mean spore lengths of P. interjectum: ", mean(spore_lengths_interjectum))
print("Mean spore widths of P. interjectum: ", mean(spore_widths_interjectum))
print("Mean basal cell count of sporangia in P. interjectum: ", mean(sporangia_basal_cell_count_interjectum))
print("Mean annulus cell count of sporangia in P. interjectum: ", mean(sporangia_annulus_cell_count_interjectum), "\n")


def createMatrix(spore_width, spore_length, length, width, acells, bcells):
    matrix = []
    matrix.append(spore_width)
    matrix.append(spore_length)
    matrix.append(length)
    matrix.append(width)
    matrix.append(acells)
    matrix.append(bcells)
    return matrix

vulgare_matrix = createMatrix(spore_widths_vulgare, spore_lengths_vulgare, leaf_lengths_vulgare, leaf_widths_vulgare, sporangia_annulus_cell_count_vulgare, sporangia_basal_cell_count_vulgare)
interjectum_matrix = createMatrix(spore_widths_interjectum, spore_lengths_interjectum, leaf_lengths_interjectum, leaf_widths_interjectum, sporangia_annulus_cell_count_interjectum, sporangia_basal_cell_count_interjectum)

print(vulgare_matrix)
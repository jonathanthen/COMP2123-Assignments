from invasion import AlienInvasion

#index 8 to 12 count: 5
# markers = [x for x in range(-20, 41, 3)]
# c = 5

#index 3 to 7 count: 5
# markers = [-20, -10, -5, -1, 0, 1, 2, 6, 15]
# c = 5

#index 1 to 4 count: 4
# markers = [-6, -4, -3, 0, 5, 30, 40, 41, 42, 43, 99, 100, 101, 102, 111]
# c = 5

#index 14 to 17 count: 4
markers = [-100, -50, -49, -38, -34, -20, -15, -14, -10, -9, -6, -4, -3, -2, 1, 10, 20, 30]
c = 13

#index 3 to 5 count: 3
# markers = [x for x in range(-20, -2, 3)]
# c = 15

print(markers)
alien = AlienInvasion()
print("Count:", alien.count_markers(markers, c))
print("Index:", alien.break_control(markers, c))


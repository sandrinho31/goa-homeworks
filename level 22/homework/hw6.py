
celestial_bodies = ["მზე", "მთვარე", "მარსი", "ვენერა", "იუპიტერი", "სატურნი", "ურანი", "ნეპტუნი", "პლუტონი", "ერისი"]
even_index_bodies = [celestial_bodies[i] for i in range(len(celestial_bodies)) if i % 2 == 0]
print(even_index_bodies)
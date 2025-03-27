import os
import time

counter = 0
skip_counter = 0
jpg = ('.jpg', '.jpeg', '.JPG')
png = ('.png', '.PNG')

# Loop through all files in the current directory
# If the file is a .jpg or .png file, rename it to 1.jpg, 2.jpg, etc.
# Currently has a bug where it will rename files that it believes do not exist if you run it a
# second time, despite the file actually existing.
# I believe this happens because it does not find files in the same order every time.
# e.g it will do everything correctly the first pass, but the next pass
# it may grab '15.jpg' and rename it to '2.jpg' because it found '15.jpg' first.

for files in os.listdir('.'):
    if files.casefold().endswith(jpg):
        counter += 1
        if os.path.exists(str(counter) + jpg[0]):
            print(str(counter) + jpg[0], 'already exists, skipping...')
            skip_counter += 1
            continue
        else:
            print('Renaming', files, 'to', str(counter) + jpg[0])
            os.rename(files, str(counter) + jpg[0])
            time.sleep(0.1) # Windows doesn't seem to like renaming files too quickly, so I added a delay.
    if files.casefold().endswith(png):
        counter += 1
        if os.path.exists(str(counter) + png[0]):
            print(str(counter) + png[0], 'already exists, skipping...')
            skip_counter += 1
            continue
        else:
            print('Renaming', files, 'to', str(counter) + png[0])
            os.rename(files, str(counter) + png[0])
            time.sleep(0.1) # see above

print('\nTried to change', counter, 'files, of those', skip_counter, 'were skipped.')
input('Press Enter to exit...')
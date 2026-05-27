#  FAKE NEWS GENERATOR


#--Import random module
import random
# Create subjects
subjects=[
   "Kolkata Metro",
"Bengaluru Startup",
"Mumbai Autorickshaw Union",
"Patna City",
"Delhi Authorities",
"Chennai Marina Beach",
"Lucknow’s Imambara",
"Jaipur Municipal Body",
"Kerala Backwaters",
"Hyderabad Biryani Shops",
"Indore City Council",
"Goa Tourism Board",
"Ahmedabad Riverfront Authority",
"Shillong Café",
"Nagpur Farmers",
"Varanasi Tourism Board",
"Pune Students",
"Odisha Temple Committee",
"Ranchi Zoo",
"Bhopal Authorities",
]
#Create Actions
actions=[
  "Introduces Adda Coaches with free chai and rosogolla",
"Launches app delivering idli within 3 minutes",
"Announces silent rides day using hand signals",
"Hosts world’s largest litti-chokha festival",
"Install AC benches to fight heat",
"Adds Wi-Fi-powered swings for online classes",
"To light up with drone-powered chandeliers",
"Launches pink-colored e-bicycles",
"Introduces floating cinema halls",
"Start pay with poetry scheme",
"Tests AI-powered dustbins that scold littering",
"Announces beach libraries with seashell exchange",
"Introduces Garba-themed musical fountains",
"Serves tea that changes color with live guitar music",
"Use oranges to make eco-friendly Holi colors",
"Launches Ganga boat rides with AI storytellers",
"Build scooter that runs on sugarcane juice",
"Replaces loudspeakers with conch-shaped Bluetooth devices",
"Trains parrots to mimic traffic rules",
"Set up India’s first floating cricket pitch",
]
#Create places
places=[
    "Kolkata",
"Bengaluru",
"Mumbai",
"Patna",
"Delhi (Connaught Place)",
"Chennai",
"Lucknow",
"Jaipur",
"Kerala",
"Hyderabad",
"Indore",
"Gurgaon",
"Ahmedabad (Sabarmati Riverfront)",
"Shillong",
"Nagpur",
"Varanasi",
"Pune",
"Odisha",
"Ranchi",
"Bhopal",
]

# Start the Headline Generate Loop
while True:#Means Start an Infinite Loop
    choice = input("\nDo you want a Random Headline or Custom Headline? (random/custom): ").strip().lower()
#Random Generate Headline
    if choice == "random":
        subject= random.choice(subjects)
        action= random.choice(actions )
        place= random.choice(places)
#Customer Generate Headline
    elif choice == "custom":
        subject = input("Enter the subject: ")
        action = input("Enter the action: ")
        place = input("Enter the place: ")
 #If not put full instruction
        if not subject or not action or not place:
            print(" Subject, Action, and Place cannot be empty!")
            continue
    else:
        print("Invalid choice. Please choose 'random' or 'custom'.")
        continue
#Generate Headline
    headline=f"BREAKING NEWS: {subject} {action} {place}"
    print("\n"+ headline)
  
# Ask user if they want to save the headline
    save_choice=input("\nDo You Save this Headline? (yes/no): ").strip().lower()
    if save_choice=="yes":
        with open("headlines.txt", "a") as f:
            f.write(headline + "\n")
        print("Headline saved to headlines.txt")

# Ask user if they want to generate another headline
    user_input=input("\nDo you Want to Another Headline? (yes/no): ").strip().lower()
    if user_input=="no":
        break
print("Thank You for Using Headline Generator!")


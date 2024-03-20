print("Resume")

# Personal Information
name = input("Enter your full name: ")
email = input("Enter your email address: ")
phone = input("Enter your phone number: ")

# Professional Experience
print("\nEnter your most recent job information:")
company = input("Company name: ")
role = input("Role/Position: ")
start_year = input("Start Year: ")
end_year = input("End Year or 'Present': ")
responsibilities = input("Briefly describe your responsibilities: ")

# Educational Background
print("\nEnter your highest educational attainment:")
school = input("School name: ")
degree = input("Degree: ")
graduation_year = input("Graduation Year: ")

# Skills
print("\nList three skills relevant to your job application:")
skill_1 = input("Skill 1: ")
skill_2 = input("Skill 2: ")
skill_3 = input("Skill 3: ")

#certain_resume...
print("\n----- YOUR RESUME SUMMARY -----\n")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Phone: {phone}\n")

print("Professional Experience:")
print(f"Company: {company}")
print(f"Role: {role}")
print(f"Duration: {start_year} to {end_year}")
print(f"Responsibilities: {responsibilities}\n")

print("Educational Background:")
print(f"School: {school}")
print(f"Degree: {degree}")
print(f"Graduation Year: {graduation_year}\n")

print("Skills:")
print(f"- {skill_1}")
print(f"- {skill_2}")
print(f"- {skill_3}\n")

print("Thank you")

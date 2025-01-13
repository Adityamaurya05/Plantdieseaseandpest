import streamlit as st # type: ignore

st.set_page_config(page_title="Plant and Pest Detection", layout="wide")

# Sidebar menu
st.sidebar.title("Category")
option = st.sidebar.radio("Choose a category:", ("Plants", "Pest", "Prevention"))

# Home Page Content
st.title("**Plant Diseases and Pest Detection and Prevention**")
st.write("Welcome to the Plant Diseases and Pest Detection and Prevention application! Use the sidebar to navigate.")

if option == "Plants":
    st.header("Plants")
    st.write("Learn about common, popular, and sometimes deadly plant diseases. Use the dropdown menu below to explore.")

    # Selectbox for Plant Diseases
    plant_disease_option = st.selectbox(
        "Select a Plant Disease to learn more about:",
        [
            "--Select--",
            "Powdery Mildew",
            "Downy Mildew",
            "Rusts",
            "Blights",
            "Cankers",
            "Wilts",
            "Root Rot",
            "Damping-Off",
            "Mosaic Viruses",
            "Bacterial Blights",
            "Fire Blight",
            "Panama Disease",
            "Citrus Greening",
            "Dutch Elm Disease",
            "Chestnut Blight",
        ]
    )

    # Disease Details
    if plant_disease_option == "Powdery Mildew":
        st.subheader("Powdery Mildew")
        st.write("**About:**") 
        st.write("""
        - Description: A fungal disease that coats leaves with a white, powdery substance, hindering photosynthesis.
        - Affected Plants: Roses, cucumbers, pumpkins, and many others.
        - Symptoms: White powdery spots on leaves, distorted growth, premature leaf drop.
        - Prevention: Ensure proper air circulation, avoid overhead watering, and use fungicides when necessary.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Plant Resistant Varieties (80-95%)        
        - Proper Spacing and Pruning (60-80%)
        - Avoid Overhead Watering (60-80%)
        - Maintain Adequate Plant Health (40-50%)
        - Sanitation (60-80%)         
        """)
        st.write("**Fact:** Powdery mildew fungi are unique in that they can germinate and infect plant hosts without the need for free water. This means they can thrive in dry conditions, unlike many other fungal diseases.")
        st.image("images/plants/powdery_mildew.jpg", caption="Powdery Mildew on leaves", use_column_width=True)

    elif plant_disease_option == "Downy Mildew":
        st.subheader("Downy Mildew")
        st.write("**About:**")
        st.write("""
        - Description: A fungal disease causing fuzzy, grayish-purple patches on the undersides of leaves.
        - Affected Plants: Grapes, lettuce, spinach, and other crops.
        - Symptoms: Yellowing leaves, distorted growth, and leaf drop.
        - Prevention: Use resistant plant varieties, rotate crops, and ensure good air circulation.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Plant Resistant Varieties (80-95%)
        - Proper Spacing and Pruning (70-90%)
        - Avoid Overhead Watering (70-85%)
        - Use Fungicides as Needed (60-80%)
        - Sanitation and Crop Rotation (50-75%)
        """)
        st.write("**Fact:** Downy mildew fungi produce distinctive sporangia (spore-bearing structures) that look like tiny tufts of fur on the underside of infected leaves.")
        st.image("images/plants/Downy Mildew.jpg", caption="Downy Mildew on leaves", use_column_width=True)

    elif plant_disease_option == "Rusts":
        st.subheader("Rusts")
        st.write("**About:**") 
        st.write("""
        - Description: A group of fungal diseases causing reddish-brown or orange pustules on leaves and stems.
        - Affected Plants: Roses, wheat, barley, and other crops.
        - Symptoms: Yellowing leaves, reduced growth, and yield loss.
        - Prevention: Remove infected leaves, plant resistant varieties, and apply fungicides as needed.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Plant Resistant Varieties (75-90%)
        - Remove Alternate Hosts (60-80%)
        - Proper Spacing and Ventilation (50-75%)
        - Use Preventive Fungicides (65-85%)
        - Sanitation Practices (60-80%)
        """)
        st.write("**Fact:** Rust fungi are known for their complex life cycles, often involving multiple host plants and different spore stages. Some rusts even produce spores that are different colors, such as black, brown, orange, or red.")
        st.image("images/plants/Rusts.jpg", caption="Downy Mildew on leaves", use_column_width=True)

    elif plant_disease_option == "Blights":
        st.subheader("Blights")
        st.write("**About:**")
        st.write("""
        - Description: Rapid, widespread plant death caused by various pathogens.
        - Examples: Late blight on potatoes and tomatoes (Phytophthora infestans).
        - Symptoms: Dark, water-soaked lesions on leaves and stems, followed by wilting.
        - Prevention: Use disease-free seeds, avoid overcrowding, and apply fungicides.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Certified Disease-Free Seeds (80-95%)
        - Rotate Crops Regularly (70-85%)
        - Avoid Overhead Irrigation (60-80%)
        - Remove and Destroy Infected Plant Parts (70-90%)
        - Maintain Healthy Soil and Plant Nutrition (50-70%)
        """)
        st.write("**Fact:** Blights are a broad category of plant diseases that cause rapid and severe damage, often leading to the death of plant tissues. They can be caused by fungi, bacteria, or even viruses.")
        st.image("images/plants/Blights.jpg", caption="Blight on leaves", use_column_width=True)

    elif plant_disease_option == "Cankers":
        st.subheader("Cankers")
        st.write("**About:**")
        st.write("""
        - Description: Localized dead areas on the bark of trees and shrubs, often caused by fungi.
        - Affected Plants: Fruit trees, shrubs, and ornamentals.
        - Symptoms: Sunken, discolored areas on bark, oozing sap, dieback.
        - Prevention: Prune infected branches, avoid mechanical damage, and maintain plant health.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Prune and Remove Infected Branches (60-85%)
        - Apply Protective Fungicide to Wounds (50-75%)
        - Avoid Mechanical Injuries to Plants (40-60%)
        - Use Resistant Varieties (70-90%)
        - Improve Drainage Around Roots (50-70%)
        """)
        st.write("**Fact:** Cankers are sunken, dead areas on the bark or stems of woody plants. They can be caused by various pathogens, including fungi and bacteria.")
        st.image("images/plants/Cankers.jpg", caption="Cranker on a fruit", use_column_width=True)

    elif plant_disease_option == "Wilts":
        st.subheader("Wilts")
        st.write("**About:**")
        st.write("""
        - Description: Diseases that cause plants to droop and wilt due to vascular system blockage.
        - Examples: Fusarium wilt, Verticillium wilt.
        - Affected Plants: Tomatoes, peppers, and other crops.
        - Symptoms: Wilting, yellowing leaves, stunted growth.
        - Prevention: Rotate crops, plant resistant varieties, and improve soil drainage.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Resistant Cultivars (75-95%)
        - Maintain Proper Soil Drainage (70-85%)
        - Rotate Crops with Non-Susceptible Plants (60-80%)
        - Sanitize Tools and Equipment (65-85%)
        - Improve Soil Organic Matter (50-70%)
        """)
        st.write("**Fact:** Wilts are plant diseases that cause the sudden collapse of plant tissues due to the disruption of water transport. They can be caused by fungi, bacteria, or even nematodes.")
        st.image("images/plants/Wilts.jpg", caption="Wilts on a tree", use_column_width=True)

    elif plant_disease_option == "Root Rot":
        st.subheader("Root Rot")
        st.write("**About:**")
        st.write("""
        - Description: Fungal diseases that attack plant roots, causing them to rot and decay.
        - Affected Plants: Many plants, especially in poorly drained soils.
        - Symptoms: Yellowing leaves, wilting, stunted growth, and root discoloration.
        - Prevention: Improve soil drainage, avoid overwatering, and use resistant varieties.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Ensure Proper Drainage in Soil (75-90%)
        - Avoid Overwatering (70-85%)
        - Use Fungicides Where Necessary (60-80%)
        - Sanitize Tools and Containers (50-75%)
        - Improve Soil Aeration (60-80%)
        """)
        st.write("**Fact:** Root rot is a common plant disease that affects the roots of plants, causing them to rot and decay. This can lead to stunted growth, wilting, and even death of the plant.")
        st.image("images/plants/Root Rot.jpg", caption="Roots rooten due to root rot", use_column_width=True)

    elif plant_disease_option == "Damping-Off":
        st.subheader("Damping-Off")
        st.write("**About:**")
        st.write("""
        - Description: A group of diseases that kill seedlings before or after they emerge from the soil.
        - Affected Plants: Seedlings of many plant species.
        - Symptoms: Seedlings collapse, discoloration at the soil line.
        - Prevention: Use sterilized soil, avoid overwatering, and ensure good ventilation.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Sterilized Soil or Potting Mix (80-95%)
        - Avoid Overwatering Young Seedlings (70-85%)
        - Apply Biological Controls (60-80%)
        - Provide Good Air Circulation (65-85%)
        - Use Treated or Resistant Seeds (70-90%)
        """)
        st.write("**Fact:** Damping-off is a disease that affects young seedlings, causing them to collapse and die. It is often caused by soil-borne fungi.")
        st.image("images/plants/Damping off.jpg", caption="Damping off Illustraion", use_column_width=True)

    elif plant_disease_option == "Mosaic Viruses":
        st.subheader("Mosaic Viruses")
        st.write("**About:**")
        st.write("""
        - Description: Cause mottled or discolored leaves, stunted growth, and reduced yield.
        - Examples: Tomato mosaic virus, cucumber mosaic virus.
        - Symptoms: Mottled patterns on leaves, stunted growth, poor fruit quality.
        - Prevention: Use virus-free seeds, remove infected plants, and control insect vectors.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Virus-Free Planting Material (85-95%)
        - Control Vector Insects Like Aphids (70-90%)
        - Remove Infected Plants Immediately (65-85%)
        - Avoid Handling Plants When Wet (60-80%)
        - Rotate Crops Regularly (70-85%)
        """)
        st.write("**Fact:** Mosaic viruses are plant viruses that cause mottled or mosaic-like patterns on leaves and other plant parts. They can also cause other symptoms, such as stunted growth and distorted leaves.")
        st.image("images/plants/Mosaic Viruses.jpg", caption="Mosaic Virus on a Leave", use_column_width=True)

    elif plant_disease_option == "Bacterial Blights":
        st.subheader("Bacterial Blights")
        st.write("**About:**")
        st.write("""
        - Description: Cause water-soaked lesions on leaves and stems, often with a bacterial ooze.
        - Affected Plants: Beans, tomatoes, and other crops.
        - Symptoms: Dark, wet-looking spots on leaves and stems.
        - Prevention: Use clean seeds, rotate crops, and apply bactericides when necessary.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Resistant Varieties (75-90%)
        - Avoid Overhead Irrigation (60-80%)
        - Rotate Crops and Avoid Monoculture (65-85%)
        - Remove and Destroy Infected Plants (70-90%)
        - Sanitize Equipment and Tools (60-80%)
        """)
        st.write("**Fact:** Bacterial blights are plant diseases caused by bacteria that cause the rapid death of plant tissues. They often appear as water-soaked lesions on leaves and stems.")
        st.image("images/plants/Bacterial Blights.jpg", caption="Bacterial Blights on a Leave", use_column_width=True)

    elif plant_disease_option == "Fire Blight":
        st.subheader("Fire Blight")
        st.write("**About:**")
        st.write("""
        - Description: A bacterial disease that affects apples, pears, and other fruit trees.
        - Symptoms: Blackened, scorched appearance of branches and leaves.
        - Prevention: Prune infected branches, apply copper-based sprays, and avoid wetting foliage.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Plant Resistant Varieties (70-90%)
        - Prune Infected Branches Below the Infection Line (60-80%)
        - Avoid Excessive Nitrogen Fertilization (50-75%)
        - Apply Copper-Based Bactericides (60-80%)
        - Sanitize Pruning Tools Regularly (70-85%)
        """)
        st.write("**Fact:** Fire blight is a bacterial disease that affects members of the rose family, such as apples, pears, and roses. It causes the infected plant parts to appear scorched or burned, hence the name.")
        st.image("images/plants/Fire Blight.jpg", caption="Fire Blight on a Leave", use_column_width=True)

    elif plant_disease_option == "Panama Disease":
        st.subheader("Panama Disease")
        st.write("**About:**")
        st.write("""
        - Description: A devastating fungal disease that affects bananas.
        - Symptoms: Wilting, yellowing leaves, stunted growth.
        - Prevention: Use resistant varieties, maintain soil health, and avoid contaminated tools.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Resistant Banana Varieties (80-95%)
        - Practice Proper Field Sanitation (70-85%)
        - Avoid Moving Contaminated Soil (65-85%)
        - Rotate with Non-Susceptible Crops (60-80%)
        - Improve Soil Drainage (70-90%)
        """)
        st.write("**Fact:** Panama disease is a fungal disease that affects bananas. It causes the roots to rot, leading to the collapse and death of the plant")
        st.image("images/plants/Panama Disease.jpg", caption="Panama Disease on a Leave", use_column_width=True)

    elif plant_disease_option == "Citrus Greening":
        st.subheader("Citrus Greening")
        st.write("**About:**")
        st.write("""
        - Description: A bacterial disease that affects citrus trees.
        - Symptoms: Bitter, misshapen fruit, yellowing leaves.
        - Prevention: Control insect vectors, use resistant rootstocks, and remove infected trees.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Plant Certified Disease-Free Trees (85-95%)
        - Control Vector Insects Like Psyllids (75-90%)
        - Remove and Destroy Infected Trees (65-85%)
        - Use Nutritional Supplements for Tree Health (50-70%)
        - Monitor Orchards Regularly for Symptoms (70-85%)
        """)
        st.write("**Fact:**  Citrus greening is a bacterial disease that affects citrus trees. It causes the fruit to become misshapen and bitter, and eventually leads to the death of the tree.")
        st.image("images/plants/Citrus Greening.jpg", caption="Citrus Greening on a fruit", use_column_width=True)

    elif plant_disease_option == "Dutch Elm Disease":
        st.subheader("Dutch Elm Disease")
        st.write("**About:**")
        st.write("""
        - Description: A fungal disease that affects elm trees.
        - Symptoms: Wilting, yellowing leaves, dieback.
        - Prevention: Prune infected branches, control beetle vectors, and use resistant varieties.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Disease-Resistant Elm Varieties (80-95%)
        - Remove and Destroy Infected Wood (70-90%)
        - Control Bark Beetles, the Disease Vectors (65-85%)
        - Apply Fungicides to High-Value Trees (60-80%)
        - Avoid Pruning During Active Beetle Season (60-80%)
        """)
        st.write("**Fact:** Dutch elm disease is a fungal disease that affects elm trees. It is spread by bark beetles and causes the leaves to wilt and the tree to die.")
        st.image("images/plants/Dutch Elm Disease.jpg", caption="Dutch Elm Disease on a Leave", use_column_width=True)

    elif plant_disease_option == "Chestnut Blight":
        st.subheader("Chestnut Blight")
        st.write("**About:**")
        st.write("""
        - Description: A fungal disease that nearly wiped out American chestnut trees.
        - Symptoms: Sunken cankers, dieback, and tree death.
        - Prevention: Plant resistant varieties and remove infected trees.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Resistant Chestnut Hybrids (80-95%)
        - Prune and Remove Cankers (70-85%)
        - Avoid Wounding the Trees (60-80%)
        - Apply Biological Control Agents (50-70%)
        - Sanitize Equipment and Tools (60-80%)
        """)
        st.write("**Fact:** Chestnut blight is a fungal disease that devastated American chestnut trees in the early 20th century. It causes the bark to crack and the tree to die.")
        st.image("images/plants/Chestnut Blight.jpg", caption="Chestnut Blight on a Branch", use_column_width=True)
    
elif option == "Pest":
    st.header("Pest")
    st.write("Information about common pests and how to identify them.")
    
    # Catalog for pest-related recipes
    recipe_option = st.selectbox(
        "Select a Pest you wanna know about:",
        ["--Select--", "Thirps", "Wireworms", "Whitefly", "Sawfly", "Grasshopper", "Mites", "Cutworms", "Aphides", "Caterpillar", "Flea Beetle", "Army Worms", "Snails"]
    )

    if recipe_option == "Thirps":
        st.subheader("Thirps")
        st.write("**About them:**")
        st.write("""
        - What they are: Tiny, slender insects with fringed wings.
        - Common names: Thrips, thunderflies
        - Regions: Found worldwide, thriving in warm, dry climates.
        - Favorite crops: A wide range of plants, including flowers, vegetables (tomatoes, peppers), and fruits.
        - Prevention: Sticky traps to monitor populations, maintaining good garden hygiene, and using beneficial insects like predatory mites.
        - Locating: Look for tiny black or brown spots on leaves, distorted growth, and silvery streaks.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Resistant Varieties (75-90%)
        - Introduce Beneficial Predators (e.g., Ladybugs) (65-85%)
        - Apply Reflective Mulches (60-80%)
        - Use Insecticidal Soaps or Oils (60-75%)
        - Monitor and Use Sticky Traps (50-70%)
        """)
        st.write("**Fact:** Thrips have unique fringed wings that allow them to fly short distances and even hover.")
        st.image("images/pests/thrips.jpeg", caption="Thrips on leaves", use_column_width=True)
        
    elif recipe_option == "Wireworms":
        st.subheader("Wireworms")
        st.write("**About Them:**")
        st.write("""
        - What they are: Larvae of click beetles, slender and hard-bodied.   
        - Common names: Wireworms, leather jackets   
        - Regions: Widely distributed, particularly prevalent in areas with heavy soil and high organic matter.
        - Favorite crops: Corn, potatoes, and other root vegetables.
        - Prevention: Crop rotation, maintaining soil pH, and using nematode-based biological control.
        - Locating: Examine soil for the slender, wiry larvae.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Rotate Crops with Non-Susceptible Plants (70-85%)
        - Trap Using Bait Stations (60-80%)
        - Maintain Good Soil Drainage (65-85%)
        - Apply Biological Controls (e.g., Nematodes) (60-75%)
        - Avoid Over-Tilling Soil (50-70%)
        """)
        st.write("**Fact:** These grubs can spend years living in the soil, making them difficult to control.")
        st.image("images/pests/wireworm.jpeg", caption="Wireworms on soil", use_column_width=True)
        
    elif recipe_option == "Whitefly":
        st.subheader("Whitefly")
        st.write("**About Them:**")
        st.write("""
        - What they are: Small, winged insects with white, powdery bodies.   
        - Common names: Whitefly, greenhouse whitefly   
        - Regions: Found worldwide, thriving in warm, humid conditions.   
        - Favorite crops: Tomatoes, cucumbers, and other greenhouse plants.
        - Prevention: Yellow sticky traps, introducing beneficial insects like ladybugs, and using insecticidal soap.
        - Locating: Look for the tiny white insects on the undersides of leaves.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Yellow Sticky Traps (70-85%)
        - Encourage Natural Predators (e.g., Parasitic Wasps) (65-85%)
        - Apply Neem Oil or Insecticidal Soaps (60-80%)
        - Remove Weeds and Alternate Hosts (60-75%)
        - Monitor and Control Infestation Early (50-70%)
        """)
        st.write("**Fact:** Whiteflies produce a sticky substance called honeydew, which can attract sooty mold.")
        st.image("images/pests/whitefly.jpg", caption="Whitefly on grass", use_column_width=True)
        
    elif recipe_option == "Sawfly":
        st.subheader("Sawfly")
        st.write("**About Them:**")
        st.write("""
        - What they are: Larvae of sawflies, resembling caterpillars but with more legs.
        - Common names: Sawfly larvae, slugworms
        - Regions: Found worldwide, particularly in temperate regions.
        - Favorite crops: Roses, currants, gooseberries, and other woody plants.
        - Prevention: Handpicking larvae, using insecticidal soap, and introducing parasitic wasps.
        - Locating: Look for the larvae feeding on leaves, often skeletonizing them.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Prune and Remove Infested Leaves (65-85%)
        - Apply Horticultural Oils or Insecticides (60-75%)
        - Introduce Beneficial Parasitoids (e.g., Wasps) (60-80%)
        - Monitor Regularly During Larval Stages (50-70%)
        - Use Resistant Plant Varieties (70-90%)
        """)
        st.write("**Fact:** Sawfly larvae have more legs than caterpillars, typically 6-8 pairs compared to 5 pairs for caterpillars.")
        st.image("images/pests/Sawfly.jpg", caption="Sawfly on Leave", use_column_width=True)
        
    elif recipe_option == "Grasshopper":
        st.subheader("Grasshopper")
        st.write("**About Them:**")
        st.write("""
        - What they are: Jumping insects with powerful hind legs.
        - Common names: Grasshopper, locust
        - Regions: Found worldwide, particularly in dry, grassy areas.
        - Favorite crops: A wide range of plants, including grasses, cereals, and vegetables.
        - Prevention: Maintaining a clean garden, using row covers, and introducing natural predators like birds.
        - Locating: Look for the large, jumping insects in fields and gardens.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Create Trap Crops as Decoys (70-85%)
        - Encourage Birds and Predators (65-85%)
        - Apply Biological Pesticides (e.g., Nosema locustae) (60-80%)
        - Remove Weeds and Brushy Areas (60-75%)
        - Use Insecticidal Sprays if Necessary (50-70%)
        """)
        st.write("**Fact:** Some grasshopper species can change color to blend in with their surroundings, a remarkable form of camouflage.")
        st.image("images/pests/grass.jpg", caption="Grasshopper on a leave", use_column_width=True)
        
    elif recipe_option == "Mites":
        st.subheader("Mites")
        st.write("**About Them:**")
        st.write("""
        - What they are: Tiny arachnids, often microscopic.   
        - Common names: Spider mites, two-spotted spider mites
        - Regions: Found worldwide, thriving in warm, dry conditions.
        - Favorite crops: Many plants, including roses, tomatoes, and beans.
        - Prevention: Maintaining proper humidity, using insecticidal soap, and introducing predatory mites.
        - Locating: Look for fine webbing on leaves and tiny red or brown spots.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Spray with Miticides or Horticultural Oils (70-85%)
        - Maintain High Humidity to Deter Spider Mites (65-80%)
        - Introduce Beneficial Predators (e.g., Ladybugs) (60-80%)
        - Avoid Over-Fertilizing Plants (50-75%)
        - Monitor and Remove Affected Leaves (50-70%)
        """)
        st.write("**Fact:** While many mites are pests, some are beneficial predators that feed on other harmful insects.")
        st.image("images/pests/mite.jpg", caption="Mite on a leave", use_column_width=True)
        
    elif recipe_option == "Cutworms":
        st.subheader("Cutworms")
        st.write("**About Them:**")
        st.write("""
        - What they are: Larvae of various moth species, typically nocturnal and soil-dwelling.   
        - Common names: Cutworms, armyworms   
        - Regions: Found worldwide, particularly in areas with high organic matter in the soil.
        - Favorite crops: Young seedlings and transplants of many vegetables and flowers.   
        - Prevention:
            - Physical Barriers: Collars around young plants to prevent them from climbing.   
            - Soil Cultivation: Deep tillage to expose pupae to predation.
            - Crop Rotation: Avoid planting susceptible crops in the same area year after year.   
            - Beneficial Insects: Encourage natural predators like birds and ground beetles.   
        - Locating:
            - Look for cut marks at or just below the soil line on young plants.
            - Inspect the soil around plants at night with a flashlight to spot the cutworms.
            - Handpick cutworms from around plants in the evening
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Collars Around Seedlings (70-90%)
        - Remove Weeds and Plant Debris (65-85%)
        - Apply Beneficial Nematodes (60-80%)
        - Handpick at Night Where Visible (50-75%)
        - Till Soil to Disrupt Pupae (50-70%)
        """)
        st.write("**Fact:** Cutworms are most active at night, so it's best to inspect for them in the evening or early morning.")
        st.image("images/pests/cutworm.jpg", caption="Cutworm on a leave", use_column_width=True)
        
    elif recipe_option == "Aphides":
        st.subheader("Aphides")
        st.write("**About Them:**")
        st.write("""
        - What they are: Small, pear-shaped insects that suck sap from plants.
        - Common names: Aphids, plant lice
        - Regions: Found worldwide, thriving in warm, humid conditions. 
        - Favorite crops: A wide range of plants, including roses, vegetables, and fruits.
        - Prevention: Introducing ladybugs and other natural predators, using insecticidal soap, and planting companion plants.
        - Locating: Look for the small, soft-bodied insects on stems and leaves.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Introduce Natural Predators (e.g., Ladybugs) (70-90%)
        - Spray Plants with Neem Oil or Soapy Water (65-85%)
        - Use Reflective Mulches to Repel Aphids (60-75%)
        - Remove Infested Leaves and Stems (60-80%)
        - Apply Companion Planting (e.g., Garlic) (50-70%)
        """)
        st.write("**Fact:** Aphids can reproduce asexually, meaning a single female can produce a large population very quickly.")
        st.image("images/pests/aphids.jpeg", caption="Aphide on a leave", use_column_width=True)
        
    elif recipe_option == "Caterpillar":
        st.subheader("Caterpillar")
        st.write("**About Them:**")
        st.write("""
        - What they are: Larvae of moths and butterflies, often voracious eaters.
        - Common names: Caterpillars, worms
        - Regions: Found worldwide, with different species in various regions.
        - Favorite crops: A wide range of plants, depending on the species.
        - Prevention: Handpicking caterpillars, using row covers, and introducing natural predators like birds.
        - Locating: Look for the larvae feeding on leaves and stems.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Bacillus thuringiensis (Bt) Spray (70-90%)
        - Introduce Parasitic Wasps or Predators (65-85%)
        - Remove Eggs and Larvae by Hand (60-75%)
        - Cover Crops with Floating Row Covers (60-80%)
        - Monitor and Remove Infested Plants (50-70%)
        """)
        st.write("**Fact:** Caterpillars have incredible growth rates and can increase their size many times over during their development.")
        st.image("images/pests/caterpillars.jpeg", caption="Caterpillar on a leave", use_column_width=True)
        
    elif recipe_option == "Flea Beetle":
        st.subheader("Flea Beetle")
        st.write("**About Them:**")
        st.write("""
        - What they are: Small, jumping beetles that feed on leaves.
        - Common names: Flea beetles
        - Regions: Found worldwide, thriving in warm, dry conditions.
        - Favorite crops: Cruciferous vegetables like cabbage, broccoli, and kale.
        - Prevention: Row covers, using insecticidal soap, and planting companion plants like marigolds.   
        - Locating: Look for the tiny, jumping beetles on leaves, often leaving small holes.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Apply Row Covers to Protect Plants (70-85%)
        - Use Sticky Traps Near Crops (65-80%)
        - Introduce Predators like Ground Beetles (60-80%)
        - Avoid Early Season Planting (60-75%)
        - Rotate Crops Regularly (50-70%)
        """)
        st.write("**Fact:** These tiny beetles are strong jumpers, hence their name.")
        st.image("images/pests/flea beetle.jpeg", caption="Flea Beetle on a leave", use_column_width=True)
        
    elif recipe_option == "Army Worms":
        st.subheader("Army Worms")
        st.write("**About Them:**")
        st.write("""
        - What they are: Larvae of armyworm moths, known for their destructive feeding habits.
        - Common names: Armyworms, cutworms
        - Regions: Found worldwide, particularly in areas with grassy fields.
        - Favorite crops: Corn, wheat, and other grasses.
        - Prevention: Crop rotation, using resistant varieties, and introducing natural predators like birds.
        - Locating: Look for the larvae feeding on leaves and stems, often in large numbers.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Bacillus thuringiensis (Bt) Spray (70-90%)
        - Encourage Birds and Natural Predators (65-85%)
        - Apply Beneficial Nematodes to Soil (60-80%)
        - Monitor Fields Regularly for Egg Masses (60-75%)
        - Remove Weeds to Limit Breeding Grounds (50-70%)
        """)
        st.write("**Fact:** Armyworms are known for their destructive feeding habits and their tendency to move in large groups.")
        st.image("images/pests/armyworms.jpg", caption="Army Worm on a leave", use_column_width=True)
        
    elif recipe_option == "Snails":
        st.subheader("Snails")
        st.write("**About Them:**")
        st.write("""
        - What they are: Mollusks with a hard shell.
        - Common names: Snails, slugs   
        - Regions: Found worldwide, thriving in moist, shady environments.
        - Favorite crops: A wide range of plants, including lettuce, strawberries, and flowers.
        - Prevention: Creating barriers like copper tape, using snail bait, and introducing natural predators like ducks.
        - Locating: Look for the slimy trails they leave behind on plants and the ground.
        """)
        st.write("**Prevention:**")
        st.write("""
        - Use Physical Barriers Like Copper Tape (70-90%)
        - Remove Mulch and Debris from Around Plants (65-85%)
        - Apply Organic Baits or Traps (60-80%)
        - Encourage Predators Like Ducks or Birds (60-75%)
        - Handpick Snails During Wet Weather (50-70%)
        """)
        st.write("**Fact:** Snails are hermaphrodites, meaning they have both male and female reproductive organs.")
        st.image("images/pests/snail.jpg", caption="Snail on a Plant", use_column_width=True)

elif option == "Prevention":
    st.header("Prevention")
    st.write("Strategies for preventing pest infestations and promoting plant health.")

    # Catalog for prevention methods
    Prevention_option = st.selectbox(
        "Select the Prevention Method you want to know about:",
        ["--Select--", "Plant Health Management", "Cultural Practices", "Soil Management", "Physical Barriers", 
         "Biological Control", "Chemical Control", "Monitoring and Early Detection", "Plant Resistance", 
         "Sanitation", "Quarantine", "Companion Planting", "Diversify Your Garden", "Water Wisely", 
         "Fertilize Properly", "Stay Informed"]
    )

    if Prevention_option == "Plant Health Management":
        st.subheader("Plant Health Management")
        st.write("""
        **About:** Keeping plants healthy to prevent pest outbreaks.
        **Key Points:**
        - Regularly inspect plants for early signs of stress or pest damage.
        - Prune dead or infected parts of the plant.
        - Provide sufficient sunlight, water, and nutrients for growth.
        """)

    elif Prevention_option == "Cultural Practices":
        st.subheader("Cultural Practices")
        st.write("""
        **About:** Altering farming and gardening practices to prevent pest buildup.
        **Key Points:**
        - Rotate crops yearly to disrupt pest life cycles.
        - Use cover crops and green manure to improve soil health.
        - Avoid overwatering, which can attract pests like fungus gnats.
        """)

    elif Prevention_option == "Soil Management":
        st.subheader("Soil Management")
        st.write("""
        **About:** Maintaining healthy soil to deter pests.
        **Key Points:**
        - Regularly test soil pH and adjust as needed.
        - Add organic matter like compost to improve soil structure and fertility.
        - Avoid over-tilling, which can disrupt beneficial soil organisms.
        """)

    elif Prevention_option == "Physical Barriers":
        st.subheader("Physical Barriers")
        st.write("""
        **About:** Creating physical barriers to block pests.
        **Key Points:**
        - Use row covers or netting to protect plants from flying insects.
        - Apply mulch to prevent soil-dwelling pests from reaching plants.
        - Use plant collars to prevent cutworm damage to seedlings.
        """)

    elif Prevention_option == "Biological Control":
        st.subheader("Biological Control")
        st.write("""
        **About:** Using natural predators or parasites to control pests.
        **Key Points:**
        - Introduce beneficial insects like ladybugs or predatory mites.
        - Release nematodes to target soil-dwelling pests.
        - Plant flowers that attract pollinators and natural predators.
        """)

    elif Prevention_option == "Chemical Control":
        st.subheader("Chemical Control")
        st.write("""
        **About:** Using pesticides as a last resort.
        **Key Points:**
        - Use organic pesticides like neem oil or insecticidal soap.
        - Always follow the label instructions to avoid harm to beneficial insects.
        - Rotate chemical classes to prevent pest resistance.
        """)

    elif Prevention_option == "Monitoring and Early Detection":
        st.subheader("Monitoring and Early Detection")
        st.write("""
        **About:** Catching pest infestations early to prevent them from spreading.
        **Key Points:**
        - Inspect plants regularly for early signs of pest activity.
        - Set up sticky traps to monitor flying insect populations.
        - Use pheromone traps for specific pest species.
        """)

    elif Prevention_option == "Plant Resistance":
        st.subheader("Plant Resistance")
        st.write("""
        **About:** Choosing pest-resistant plant varieties.
        **Key Points:**
        - Plant crops bred for resistance to common pests.
        - Use native plants adapted to local conditions.
        - Avoid monoculture planting, which can be vulnerable to pests.
        """)

    elif Prevention_option == "Sanitation":
        st.subheader("Sanitation")
        st.write("""
        **About:** Keeping the garden clean to reduce pest habitats.
        **Key Points:**
        - Remove weeds, fallen leaves, and plant debris regularly.
        - Clean gardening tools to prevent spreading pests or diseases.
        - Dispose of infected plant materials far from the garden.
        """)

    elif Prevention_option == "Quarantine":
        st.subheader("Quarantine")
        st.write("""
        **About:** Preventing pests from entering or spreading.
        **Key Points:**
        - Inspect new plants for signs of pests before adding them to your garden.
        - Isolate new plants for a few weeks to ensure they are pest-free.
        - Avoid moving infested soil or debris between garden areas.
        """)

    elif Prevention_option == "Companion Planting":
        st.subheader("Companion Planting")
        st.write("""
        **About:** Using plant partnerships to deter pests.
        **Key Points:**
        - Plant marigolds to repel nematodes and aphids.
        - Grow basil near tomatoes to deter whiteflies.
        - Use garlic or onions to repel a variety of pests.
        """)

    elif Prevention_option == "Diversify Your Garden":
        st.subheader("Diversify Your Garden")
        st.write("""
        **About:** Growing a mix of plants to confuse pests.
        **Key Points:**
        - Avoid planting large areas of the same crop (monoculture).
        - Include flowers and herbs to attract beneficial insects.
        - Use intercropping to break up pest pathways.
        """)

    elif Prevention_option == "Water Wisely":
        st.subheader("Water Wisely")
        st.write("""
        **About:** Proper watering techniques to avoid attracting pests.
        **Key Points:**
        - Water early in the morning to reduce humidity at night.
        - Avoid overhead watering, which can spread diseases.
        - Use drip irrigation to deliver water directly to plant roots.
        """)

    elif Prevention_option == "Fertilize Properly":
        st.subheader("Fertilize Properly")
        st.write("""
        **About:** Providing plants with balanced nutrition.
        **Key Points:**
        - Use organic fertilizers to avoid excessive nitrogen levels.
        - Test soil nutrient levels to avoid over-fertilizing.
        - Apply fertilizer at the right growth stage for your plants.
        """)

    elif Prevention_option == "Stay Informed":
        st.subheader("Stay Informed")
        st.write("""
        **About:** Keeping up-to-date with pest control techniques.
        **Key Points:**
        - Join local gardening groups or forums.
        - Attend workshops or read gardening books.
        - Monitor regional pest alerts to stay ahead of outbreaks.
        """)
    
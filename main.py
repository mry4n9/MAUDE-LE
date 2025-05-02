from lead_engine_generator import LeadEngineGenerator
import sys
import time
# for python

def main():
    print("=" * 60)
    print("✨ Lead Engine Content Generator ✨")
    print("=" * 60)
    
    # Start user input time measurement
    user_input_start_time = time.time()
    
    # Get OpenAI API key
    api_key = input("Enter your OpenAI API key: ").strip()
    if not api_key:
        print("❌ API key is required.")
        sys.exit(1)
    
    # Initialize generator
    try:
        generator = LeadEngineGenerator(api_key)
        print("✅ Initialized Lead Engine Generator")
    except Exception as e:
        print(f"❌ Failed to initialize: {str(e)}")
        sys.exit(1)
    
    # Get website URL
    website_url = input("Enter client's website URL: ").strip()
    if not website_url:
        print("❌ Website URL is required.")
        sys.exit(1)
    
    # Get lead purpose
    print("\nSelect lead purpose:")
    print("1. Demo Booking")
    print("2. Sales Meeting")
    choice = input("Enter choice (1-2): ").strip()
    
    lead_purpose = None
    if choice == "1":
        lead_purpose = "Demo Booking"
    elif choice == "2":
        lead_purpose = "Sales Meeting"
    else:
        print("❌ Invalid choice. Using default.")
    
    # Get asset link
    asset_link = None
    has_asset = input("\nDo you have a downloadable asset? (y/n): ").lower().strip()
    if has_asset == 'y':
        asset_link = input("Enter asset link: ").strip()
        
        # Get PDF URL for content extraction (optional)
        pdf_url = input("\nEnter PDF URL for content extraction (or leave blank): ").strip()
    else:
        pdf_url = None
    
    # Get number of posts
    try:
        num_posts = int(input("\nNumber of posts for each funnel stage (default: 3): ").strip() or "3")
    except ValueError:
        print("❌ Invalid number. Using default of 3 posts.")
        num_posts = 3
    
    # Set lead purpose if selected
    if lead_purpose:
        generator.set_lead_purpose(lead_purpose, asset_link)
        print(f"✅ Set lead purpose to: {lead_purpose}")
    
    # Select social media channels
    print("\nSelect social media channels (default: LinkedIn and Facebook):")
    print("1. LinkedIn only")
    print("2. Facebook only")
    print("3. Both LinkedIn and Facebook")
    channel_choice = input("Enter choice (1-3, default is 3): ").strip() or "3"
    
    channels = []
    if channel_choice == "1":
        channels = ["LinkedIn"]
    elif channel_choice == "2":
        channels = ["Facebook"]
    else:  # Default to both
        channels = ["LinkedIn", "Facebook"]
    
    # End of user input time measurement
    user_input_time = time.time() - user_input_start_time
    minutes, seconds = divmod(user_input_time, 60)
    print(f"\n⏱️ User input completed in {int(minutes)} minutes and {int(seconds)} seconds")
    
    # Start automation time measurement
    automation_start_time = time.time()
    
    # Generate content
    print("\n" + "=" * 60)
    print("Generating content funnel... This may take a few minutes.")
    print("=" * 60)
    
    success = generator.generate_funnel_content(website_url, pdf_url, num_posts, channels)
    
    if success:
        # Export to Excel
        excel_path = generator.export_to_excel()
        if excel_path:
            print(f"\n✅ Content funnel successfully generated and saved to:")
            print(f"📊 {excel_path}")
        else:
            print("\n❌ Failed to export content to Excel.")
    else:
        print("\n❌ Failed to generate content funnel.")
    
    # Calculate and display automation time
    automation_time = time.time() - automation_start_time
    minutes, seconds = divmod(automation_time, 60)
    print(f"\n⏱️ Automation completed in {int(minutes)} minutes and {int(seconds)} seconds")
    
    # User input time reporting (moved from earlier so it appears at the end)
    minutes, seconds = divmod(user_input_time, 60)
    print(f"⏱️ User input time: {int(minutes)} minutes and {int(seconds)} seconds")
    
    print("\nThank you for using Lead Engine Content Generator!\n")

if __name__ == "__main__":
    main()
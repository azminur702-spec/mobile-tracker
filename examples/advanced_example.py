"""Advanced example of using PhoneTracker"""

import sys
sys.path.insert(0, '..')

from src.phone_tracker import PhoneTracker


def main():
    tracker = PhoneTracker()
    
    # Example phone numbers with different regions
    test_cases = [
        ("+919876543210", None),        # India (full format)
        ("0821-1234-5678", "ID"),       # Indonesia
        ("0895-1234-5678", "ID"),       # Indonesia
        ("+62821123456", None),         # Indonesia (full format)
    ]
    
    print("📱 ADVANCED MOBILE TRACKER EXAMPLES\n")
    
    for phone_number, region in test_cases:
        print(f"\n🔍 Checking: {phone_number} (Region: {region or 'Auto-detect'})")
        print("-" * 60)
        
        info = tracker.get_detailed_info(phone_number, region)
        if info:
            tracker.print_info(info)
        else:
            print(f"❌ Could not retrieve information for {phone_number}\n")


def batch_example():
    """Example of batch processing multiple numbers"""
    tracker = PhoneTracker()
    
    numbers = [
        "+919876543210",
        "+1-541-754-3010",
        "+44-20-7946-0958",
    ]
    
    print("\n📋 BATCH CHECK EXAMPLE\n")
    results = tracker.batch_check(numbers)
    
    for result in results:
        if result:
            print(f"✅ {result['phone_number']}")
            print(f"   Location: {result['location']}")
            print(f"   Carrier: {result['carrier']}")
        print()


if __name__ == "__main__":
    main()
    batch_example()

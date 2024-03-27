import argparse
from utils import Utils

def run_all(year,top_dealer,top_brands):
    utl = Utils()

    data = utl.data_manipulation(utl.get_data())
    utl.save_to_file(data)
    utl.print_info(data)
    utl.get_top_by_brands(data, top_brand=3)
    utl.get_count_by_years(data)
    utl.get_top_dealers(data, top_dealer=5)
    utl.avg_price_by_year(data)
    utl.price_distribution(data)
    utl.avg_mileage_by_model(data)
    utl.avg_price_by_dealer(data)
    utl.budget_segments(data)
    utl.get_top20cars(data)
    utl.get_total_sales_by_year(data, year=2022)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cars")
    parser.add_argument("--year", type=int)
    parser.add_argument("--top_dealer", type=int)
    parser.add_argument("--top_brands", type=int)


    args = parser.parse_args()
    run_all(year=args.year,
            top_dealer=args.top_dealer,
            top_brands=args.top_brands
            )
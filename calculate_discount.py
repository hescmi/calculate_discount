import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=int, help="original cost of the item")
    parser.add_argument("pdis", type=int, help="percentage discount given on the item", default=0)
    parser.add_argument("ddis", type=int, help="fixed dollar discount taken off the price of the product after percent discount ", default=0)
    args = vars(parser.parse_args())
#    print args

    dis_cost = discountGen(args)
    print dis_cost

def discountGen(item_info):
    item_cost = int(item_info["price"])
    per_dis = int(item_info["pdis"])
    abs_dis = int(item_info["ddis"])
    dis_cost = ((item_cost - (item_cost * (per_dis * 0.01))) - abs_dis)
    return dis_cost

if __name__ == "__main__":
    main()

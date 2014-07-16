import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=int, help="original cost of the item")
    parser.add_argument("pdis", type=int, help="percentage discount given on the item", default=0)
    parser.add_argument("ddis", type=int, help="fixed dollar discount taken off the price of the product after percent discount ", default=0)
    args = vars(parser.parse_args())
#    print args

    dis_cost = discountGen(args)
    if dis_cost > 1:
        print "The price of the item is ${0:.2f} after discount.".format(dis_cost)
    else:
        print "This is a super saver item for ${0:.2f}! What a deal!".format(dis_cost)

def discountGen(item_info):
    item_cost = int(item_info["price"])
    per_dis = int(item_info["pdis"])
    abs_dis = int(item_info["ddis"])
    dis_cost = ((item_cost - (item_cost * (per_dis * 0.01))) - abs_dis)
    if dis_cost <= 0:
        return 1
    else:
        return dis_cost

if __name__ == "__main__":
    main()

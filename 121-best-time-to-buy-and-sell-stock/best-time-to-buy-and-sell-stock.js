/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {

    let cheapest = prices[0];
    let max_profit = 0;

    for (let i=0 ; i<prices.length;i++){
        
        if (prices[i] < cheapest){
            cheapest = prices[i];
            
        }
        let profit_today = prices[i] - cheapest;
        if(profit_today > max_profit){
            max_profit = profit_today;
        }


    }
    return max_profit;

};
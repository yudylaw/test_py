#!/usr/bin/env python
# coding=utf-8

if __name__ == "__main__":
    # 充值
    pay_diamond = 2989130
    # 消耗
    cost_diamond = 2942308
    # 留存
    remain_diamond = 2313657
    # 提现
    withdraw_ticket = 2978060
    # 留存
    remain_ticket = 436834
    # 奖励
    reward_diamond = 262400
    reward_ticket = 374380
    # 运营成本
    op_cost_diamond = 1998000
    op_cost_ticket = 108000

    diff_diamond = (pay_diamond + reward_diamond + op_cost_diamond) - cost_diamond - remain_diamond

    diff_ticket = (cost_diamond + reward_ticket + op_cost_ticket) - withdraw_ticket - remain_ticket

    print 'diff_diamond=', diff_diamond

    print 'diff_ticket=', diff_ticket

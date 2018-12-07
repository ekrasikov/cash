import Vue from 'vue'
import Router from 'vue-router'
import ExpenseForm from '@/components/ExpenseForm'
import ExpenseList from '@/components/ExpenseList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Add expense',
      component: ExpenseForm
    }, {
      path: '/list',
      name: 'List expenses',
      component: ExpenseList
    }
  ]
})

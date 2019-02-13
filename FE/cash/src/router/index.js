import Vue from 'vue'
import Router from 'vue-router'
import ExpenseForm from '@/components/ExpenseForm'
import ExpenseList from '@/components/ExpenseList'
import LoginPage from '@/components/LoginPage'
import Callback from '@/components/Callback'
import auth from './../utils/auth'

Vue.use(Router)

function requireAuth (to, from, next) {
  if (!auth.isAuthenticated()) {
    next({
      name: 'Login'
    })
  } else {
    next()
  }
}

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      redirect: { name: 'Login' }
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginPage
    },
    {
      path: '/add',
      name: 'Add expense',
      beforeEnter: requireAuth,
      component: ExpenseForm
    },
    {
      path: '/list',
      name: 'List expenses',
      beforeEnter: requireAuth,
      component: ExpenseList
    },
    {
      path: '/callback',
      name: 'callback',
      component: Callback
    }
  ]
})

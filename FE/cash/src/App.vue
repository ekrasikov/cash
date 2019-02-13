<template>
  <div id="app">
    <section class="hero is-light is-fullheight" id="root">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="column is-6 is-offset-3">
            <!-- <h3 class="title has-text-grey">
                Cash!
            </h3>
            <p class="subtitle has-text-grey">
                Simple expense app
            </p> -->
            <nav class="navbar" role="navigation" aria-label="main navigation">
              <div class="navbar-brand">
                <p class="navbar-item has-text-grey">
                  <b>Cash!</b>
                </p>
                <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false"
                  @click="showNav = !showNav" :class="{ 'is-active': showNav }">
                  <span aria-hidden="true"></span>
                  <span aria-hidden="true"></span>
                  <span aria-hidden="true"></span>
                </a>
              </div>
              <div id="myNavbar" class="navbar-menu" :class="{ 'is-active': showNav}">
                <div class="navbar-start">
                  <router-link to='/login' class="navbar-item">
                    Home
                  </router-link>
                  <router-link v-if="authenticated" to='/add' class="navbar-item">
                    Add expense
                  </router-link>
                  <router-link v-if="authenticated" to='/list' class="navbar-item">
                    List expenses
                  </router-link>
                </div>
              </div>
            </nav>
            <div class="box">
                <router-view
                  :auth="auth"
                  :authenticated="authenticated">
                </router-view>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

import ExpenseForm from './components/ExpenseForm.vue'
import ExpenseList from './components/ExpenseList.vue'
import LoginPage from './components/LoginPage.vue'
import Callback from './components/Callback.vue'

import auth from './utils/auth'

export default {
  name: 'app',
  data: () => {
    return {
      showNav: false,
      auth,
      authenticated: auth.authenticated
    }
  },
  components: {
    ExpenseForm,
    ExpenseList,
    LoginPage,
    Callback
  },
  created () {
    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })

    if (auth.getAuthenticatedFlag() === 'true') {
      auth.renewSession()
    }
  },
  methods: {
    login () {
      auth.login()
    },
    logout () {
      auth.logout()
    }
  }
}
</script>

<style lang="css">
    @import '../node_modules/bulma/css/bulma.css';
</style>

<template>
  <div id="app">
    <section class="hero is-light is-fullheight" id="root">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="column is-6 is-offset-3">
            <h3 class="title has-text-grey">
                Cash!
            </h3>
            <p class="subtitle has-text-grey">
                Simple expense app
            </p>
            <nav class="navbar" role="navigation" aria-label="main navigation">
              <div id="myNavbar" class="navbar-menu">
                <div class="navbar-start">
                  <router-link to='/' class="navbar-item">
                    Add expense
                  </router-link>
                  <router-link to='/list' class="navbar-item">
                    List expenses
                  </router-link>
                </div>
              </div>
            </nav>
            <div class="box">
                <router-view></router-view>
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

export default {
  name: 'app',
  components: {
    ExpenseForm,
    ExpenseList
  }
}
</script>

<style lang="css">
    @import '../node_modules/bulma/css/bulma.css';
</style>

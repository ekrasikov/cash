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
            <div class="box">
                <expense-form @form-submitted="addExpense"
                              :categories="this.loadExpenseCategories()"
                              :users="this.loadUsers()">
                </expense-form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

import axios from 'axios';

import ExpenseForm from './components/ExpenseForm.vue';
import { HTTP } from './http_common.js'

export default {
  name: 'app',
  components: {
    ExpenseForm
  },
  data() {
    return {

    }
  },
  methods: {
    addExpense(expense) {
        let payload = {
            "date": expense.date,
            "user_id": expense.selectedUser,
            "category_id": expense.selectedCategory,
            "amount": expense.amount,
            "comment": expense.comment
        }
        console.log(payload)
        HTTP.post('/expenses', payload)
        .then(function (response) {
            //console.log(response);
            alert("Expense successfully added")
        })
        .catch(function (error) {
            alert(error)
        })
    },
    loadExpenseCategories() {
      var result = [];
      HTTP.get('/categories')
      .then(function (response) {
        response.data.forEach(function(item, index, array) {
          result.push(item);
        });
      })
      .catch(function (error) {
          console.log(error);
      });
      return result;
    },
    loadUsers() {
      let result = []
      HTTP.get('/users')
      .then(function (response) {
        response.data.forEach(function(item, index, array) {
          result.push(item)
        });
      })
      .catch(function (error) {
          console.log(error)
      });
      return result
    }
  }
}
</script>

<style lang="css">
    @import '../node_modules/bulma/css/bulma.css';
</style>
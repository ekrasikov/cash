<template>
  <div>
    <form @submit.prevent="onSubmit">
      <div class="field">
        <div class="control">
          <label v-for="user in usersList" class="radio" :key="user.id">
            <input type="radio" name="user" v-model="selectedUser" :value="user.id">
            {{ user.name }}
          </label>
        </div>
      </div>

      <div class="field">
        <div class="control">
          <input class="input is-large" placeholder="0.00 EUR" autofocus="" v-model="amount" required>
        </div>
      </div>

      <div class="field">
        <div class="control">
          <div class="select is-large is-fullwidth">
            <select v-model="selectedCategory">
              <option v-for="item in categoriesList" :value="item.id" :key="item.id">
                {{ item.name }}
              </option>
            </select>
          </div>
        </div>
      </div>

      <div class="field">
        <div class="control">
          <datepicker class="is-large" placeholder="Select date" v-model="date"
            :config="{ dateFormat: 'Y-m-d'}">
          </datepicker>
        </div>
      </div>

      <div class="field">
        <div class="control">
          <input class="input is-large" placeholder="Optional comment here" v-model="comment">
        </div>
      </div>

      <button class="button is-block is-info is-large is-fullwidth">
        Submit
      </button>

    </form>
  </div>
</template>

<script>
import Datepicker from 'vue-bulma-datepicker'
import { HTTP } from '../http_common.js'

export default {
  components: {
    Datepicker
  },
  data () {
    return {
      usersList: [],
      categoriesList: [],
      selectedUser: 1,
      selectedCategory: 1,
      amount: 0,
      date: (new Date()).toISOString(),
      comment: ''
    }
  },
  mounted: function () {
    this.$nextTick(() => {
      this.categoriesList = this.loadExpenseCategories()
      this.usersList = this.loadUsersList()
    })
  },
  methods: {
    onSubmit () {
      this.addExpense()
    },
    loadExpenseCategories() {
      let result = []
      HTTP.get('/categories')
        .then(function (response) {
          response.data.forEach((item) => {
          result.push(item)
        })
      })
        .catch(function (error) {
          alert(error)
        })
      return result
    },
    loadUsersList () {
      let result = []
      HTTP.get('/users')
      .then(function (response) {
        response.data.forEach( (item) => {
          result.push(item)
        })
      })
      .catch(function (error) {
          alert(error)
      });
      return result
    },
    addExpense () {
      let payload = {
          'date': this.date,
          'user_id': this.selectedUser,
          'category_id': this.selectedCategory,
          'amount': this.amount,
          'comment': this.comment
      }
      HTTP.post('/expenses', payload)
      .then( () => {
        this.amount = 0
        this.selectedCategory = 1
        this.comment = ''
        alert('Expense successfully added')
        //reset necessary fields on a form
      })
      .catch( (error) => {
          alert(error)
      })
    }
  }
}
</script>

<style>
</style>
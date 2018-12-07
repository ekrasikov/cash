<template>
  <div>
    <table class="table">
      <thead>
        <th>date</th>
        <th>amount</th>
        <th>category</th>
        <th>user</th>
      </thead>
      <tr v-for="expense in expenseList">
        <td>{{expense.date}}</td>
        <td>{{expense.amount}}</td>
        <td>{{expense.category}}</td>
        <td>{{expense.user}}</td>
        <td>
          <a class="delete" @click="deleteExpense($event)" :id="expense.id"></a>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import { HTTP } from '../http_common.js'

export default {
  data() {
    return {
      expenseList: []
    }
  },
  mounted: function () {
    this.$nextTick( () => {
      this.expenseList = this.loadExpenseList()
    })
  },
  methods: {
    loadExpenseList() {
      let result = [];
      HTTP.get('/expenses')
      .then(function (response) {
        response.data.forEach( (item) => {
          result.push(item)
        })
      })
      .catch(function (error) {
        alert(error)
      })
      return result;
    },
    deleteExpense(event) {
      HTTP.delete('/expenses/'+event.target.id)
      .then( () => {
        alert("Expense successfully deleted")
        this.$nextTick( () => {
          this.expenseList = this.loadExpenseList()
        })
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
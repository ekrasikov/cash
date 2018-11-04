<template>
    <div>
        <form>
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
                    <input class="input is-large" placeholder="0.00 EUR" autofocus="" v-model="amount">
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <div class="select is-large is-fullwidth">
                        <select v-model="selectedCategory">
                            <!--<option disabled value="">Please select a category</option>-->
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
                        :config="{ dateFormat: 'd-m-Y'}">
                    </datepicker>
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <input class="input is-large" placeholder="Optional comment here" v-model="comment">
                </div>
            </div>

            <button class="button is-block is-info is-large is-fullwidth"
                @click="() => this.$emit('form-submitted', this)">
                Submit
            </button>
        </form>
    </div>
</template>

<script>
import Datepicker from 'vue-bulma-datepicker'

export default {
   components: {
     Datepicker
   },
   props: [ "categories", "users" ],
   data() {
       return {
            amount: "",
            categoriesList: this.categories,
            usersList: this.users,
            selectedCategory: 1,
            selectedUser: 1,
            date: (new Date()).toString(),
            comment: ""
       }
   },
   methods: {
   }
}
</script>

<style>
</style>
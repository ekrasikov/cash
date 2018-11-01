<template>
    <div>
        <form>
            <div class="field">
                <div class="control">
                    <input class="input is-large" placeholder="0.00 EUR" autofocus="" v-model="amount">
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <div class="select is-large is-fullwidth">
                        <select v-model="category">
                            <option disabled value="">Please select a category</option>
                            <option v-for="item in categories">
                                {{ item }}
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
   props: [ "categories" ],
   data() {
       return {
            amount: "",
            category: "",
            date: (new Date()).toString(),
            comment: ""
       }
   },
   methods: {
        updated() {
            // to add - if supermarket in categories, then it, otherwise the first item
            this.category = this.categories[0];
        }  
   }
}
</script>

<style>
</style>
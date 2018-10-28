Vue.component('expense-form', {
    props: [ "categories" ],
    template: `
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

            <!--<div class="field">
                <b-datepicker class="control" placeholder="Select date" v-model="date"></b-datepicker>
            </div>-->

            <div class="field">
                <div class="control">
                    <input class="input is-large" placeholder="Optional comment here" v-model="date">
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
    `,
    data() {
        return {
            amount: "",
            category: "",
            date: new Date(),
            comment: ""
        }
    },
    methods: {
        created() {
            // to add - if supermarket in categories, then it, otherwise the first item
            this.category = this.categories[0];
        }   
    }
})

new Vue({
    el: "#root",
    methods: {
        addExpense(expense) {
            if( expense.category == "" ) {
                alert('Please select a category');
                return;
            }
//            axios.post('/expenses', {
//                amount: amount,
//                category: category,
//                date: date, //ISO format
//                comment: comment,
//                user: 'Masha'             
//            })
//            .then(function (response) {
//                console.log(response);
//            })
//            .catch(function (error) {
//                console.log(error);
//            })
            alert('You spent ' + expense.amount + ' EUR on ' + expense.date);
        },
        loadExpenseCategories() {
//            axios.get('/expense_categories')
//            .then(function (response) {
//                console.log(response);
//            })
//            .catch(function (error) {
//                console.log(error);
//            })
            return ["Supermarket", "Health", "Lunches"];
        }
    },
    
})
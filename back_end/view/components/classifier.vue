const Classifier  = {
  data () {
    return {
      loading: true,
      showSuccessText: false,
      showErrorText: false,
      showWarningText: false,
      classifiers: [],
      showPostModal: false,

      selectedClassifier: {
        old_code: null,
        code: null
      },
      newClassifier: {
        code: null
      },
      formAction: ''
    }
  },
  methods: {
    showActionText: function(action) {
      if (action === 'success') {
        this.showSuccessText = true;

        setTimeout(function() {
          this.showSuccessText = false;
        }.bind(this), 2000);
      }

      if (action === 'error') {
        this.showErrorText = true;

        setTimeout(function() {
          this.showErrorText = false;
        }.bind(this), 2000);
      }

      if (action === 'warning') {
        this.showWarningText = true;

        setTimeout(function() {
          this.showWarningText = false;
        }.bind(this), 2000);
      }
    },

    createClassifier: function() {
      const url = '/api/classifier/create';

      axios.post(url, this.newClassifier)
        .then(response => {
          this.showPostModal = false;
          this.getAllClassifiers();
          this.showActionText('success');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getAllClassifiers: function() {
      const url = '/api/classifier/read_all'

      this.loading = true;

      axios.get(url)
        .then(response => {
        if (Array.isArray(response.data.data)) {
          console.log('array');
          this.classifiers = response.data.data;
        } else {
          console.log('object');
          this.classifiers = [response.data.data];
        }

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getClassifierByCode: function(data) {
      let code = data.target.value;

      const url = `/api/classifier/read/${code}`;

      axios.get(url)
        .then(response => {
          console.log(response.data);
          this.selectedClassifier.old_code = response.data.data.code;
          this.selectedClassifier.code = response.data.data.code;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    updateClassifierByCode: function(data) {
      let code = data.target.value;

      const url = `/api/classifier/update/${code}`;

      console.log(this.selectedClassifier)

      axios.put(url, this.selectedClassifier)
        .then(response => {
          console.log(response);

          this.showPostModal = false;
          this.getAllClassifiers();
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deleteClassifierById: function(data) {
      let id = data.target.value;

      const url = `/api/classifier/delete/${id}`;

      axios.delete(url)
        .then(response => {

          this.getAllClassifiers();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    axios.get(`/api/classifier/read_all`)
      .then(response => {
        this.classifiers = response.data.data;

        this.loading = false;
      })
  },
  template: `
  <div class="container">
    <div class="header">
      <div class="row">
        <h1>
          <span>Classifier</span>
          <button v-on:click="showPostModal = true; formAction = 'Create'" type="button" class="btn yellow_button">Create</button>
          <button v-on:click="getAllClassifiers" type="button" class="btn purple_button">Reload</button>
        </h1>
      </div>
        <p v-if="showSuccessText === true" class="success_text">Success: some text for success action</p>
        <p v-if="showErrorText === true" class="error_text">Error: some text for error action</p>
        <p v-if="showWarningText === true" class="warning_text">Warning: some text for warning action</p>
    </div>

    <div v-if="loading === false" class="table-responsive">
      <table class="table table-sm table-bordered table-hover">
        <thead>
          <tr>
            <th>Code</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="classifier in classifiers">
            <td>{{ classifier.code }}</td>
            <td>
              <button v-bind:value="classifier.code" v-on:click="showPostModal = true; formAction = 'Update'; getClassifierByCode($event, classifier.code)" type="button" class="btn green_button">Edit</button>
              <button v-bind:value="classifier.code" v-on:click="deleteClassifierById" type="button" class="btn red_button">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>



    <div v-if="showPostModal">
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">{{ formAction }} Classifier</h5>
                </div>
                <div class="modal-body">
                  <p v-if="formAction === 'Update'">Code: <span>{{ selectedClassifier.old_code }}</span></p>
                  <div class="form-group">
                    <label for="classifierInputName">Code</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="classifierInputName" v-model="newClassifier.code">
                    <input v-else type="text" class="form-control" id="classifierInputName" v-model="selectedClassifier.code" value="selectedClassifier.code">
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showPostModal = false">Close</button>
                  <button v-if="formAction === 'Create'" type="button" class="btn yellow_button" @click.prevent="createClassifier()">{{ formAction }}</button>
                  <button v-else type="button" class="btn green_button" v-bind:value="selectedClassifier.old_code" @click.prevent="updateClassifierByCode">{{ formAction }}</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>


    <!-- loading spinner -->
    <div v-if="loading === true" class="spring-spinner">
      <div class="spring-spinner-part top">
        <div class="spring-spinner-rotator"></div>
      </div>
      <div class="spring-spinner-part bottom">
        <div class="spring-spinner-rotator"></div>
      </div>
    </div>

  </div>
  `
}

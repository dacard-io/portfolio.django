require('es6-promise').polyfill(); // Getting build errors in linux without this line (remember to install first)
/* As another fix for Lubuntu, I have to run this ridiculous command to make gulp watch
   work properly:

   echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

   The system apparently limits how many files can be watched by a user. This will increase
   the amount of watches a user can have. */

var gulp = require('gulp');
var plumber = require('gulp-plumber');
var gutil = require('gulp-util');
var autoprefixer = require('gulp-autoprefixer');
var minifycss = require('gulp-minify-css');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var del = require('del');
var concat = require('gulp-concat');
var sourcemaps = require('gulp-sourcemaps');
var imagemin = require('gulp-imagemin');
var pngquant = require('imagemin-pngquant');

var browserSync = require('browser-sync').create();
var reload      = browserSync.reload;

var AUTOPREFIXER_BROWSERS = [
  'ie >= 9',
  'ie_mob >= 10',
  'ff >= 30',
  'chrome >= 34',
  'safari >= 7',
  'opera >= 23',
  'ios >= 7',
  'android >= 4.4',
  'bb >= 10'
];

// Create error handler
var onError = function (err) {  
  gutil.log(gutil.colors.red('Error! Check the log'));
  console.log('\u0007'); // Making a beeping sound
  console.log(err);
  this.emit('end');
};
// ============================================================================
//  Main Tasks
// ============================================================================

// Default task is build
gulp.task('default', ['build']);

// Development task (watch alias)
gulp.task('dev', ['watch']);

// Build task
gulp.task('build', ['clean'], function() {
  gulp.start(['styles', 'scripts']);
});

// Styles task
gulp.task('styles', function() {
  return gulp.src(['static/assets/sass/main.scss'])
    .pipe(plumber({errorHandler: onError}))
    .pipe(sass())
    .pipe(autoprefixer(AUTOPREFIXER_BROWSERS))
    .pipe(minifycss())
    .pipe(concat('style.css'))
    .pipe(gulp.dest('static/assets/css/'));
});

// Scripts task
gulp.task('scripts', function() {
  return gulp.src(['static/assets/js/*.js'])
      .pipe(plumber({errorHandler: onError}))
      .pipe(sourcemaps.init())
      .pipe(concat('csc.dist.js'))
      .pipe(uglify())
      .pipe(sourcemaps.write())
      .pipe(gulp.dest('static/assets/js/min'));
});

// BrowserSync tasks
gulp.task('styles-browsersync', function() {
  return gulp.src(['static/assets/sass/main.scss'])
    .pipe(plumber({errorHandler: onError}))
    .pipe(sass())
    .pipe(autoprefixer(AUTOPREFIXER_BROWSERS))
    .pipe(minifycss())
    .pipe(concat('style.css'))
    .pipe(gulp.dest('static/assets/css/'))
    .pipe(reload({stream: true}));
});

// Scripts task
gulp.task('scripts-browsersync', function() {
  return gulp.src(['static/assets/js/*.js'])
      .pipe(plumber({errorHandler: onError}))
      .pipe(sourcemaps.init())
      .pipe(concat('csc.dist.js'))
      .pipe(uglify())
      .pipe(sourcemaps.write())
      .pipe(gulp.dest('static/assets/js/min/'))
      .pipe(reload({stream: true}));
});

// ============================================================================
//  Build Tasks
// ============================================================================

/**
 * Clean directories
 *
 * @since 0.1.0
 */
gulp.task('clean', function() {
  del([
    'static/assets/css/*.dist.css',
    'static/assets/js/min/*.dist.js'
  ]);
});

// END BUILD


// ============================================================================
//  Dev Tasks
// ============================================================================

/**
 * Execute tasks when files are changed
 *
 * @since 0.1.0
 */
var files = {
    html: '*.html'
};

gulp.task('watch', function() {
  gulp.watch('static/assets/sass/**/*.scss', ['styles']);
  gulp.watch('static/assets/js/*.js', ['scripts']);
});

gulp.task('serve', function() {
  browserSync.init({
        proxy: "localhost:8000"
  });
  
  gulp.watch('static/assets/js/**/*.js', ['scripts-browsersync']);
  gulp.watch('static/assets/sass/**/*.scss', ['styles-browsersync']);
  gulp.watch(files.html).on('change', reload);
});

// Optimize images (except PNGs)
gulp.task('imagemin', function() {
  return gulp.src('static/assets/images/**/*.*')
    .pipe(imagemin({
      progressive: true,
      svgoPlugins: [{removeViewBox: false}],
      use: [pngquant()]
    }))
    .pipe(gulp.dest('static/assets/images/'));
});
// END DEV TASKS

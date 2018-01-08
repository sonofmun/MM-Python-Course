<!-- Source : https://github.com/tonik/theme/blob/b08a6463645fdf7b9ea0b15e3eb1144af41774ab/resources/templates/partials/header.tpl.php -->

<header class="callout large">
    <?php do_action('theme/header/start') ?>

    <h2><?= $title ?></h2>
    <p class="lead"><?= $lead ?></p>

    <?php do_action('theme/header/end') ?>
</header>
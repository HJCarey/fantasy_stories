import click
import logging

from gpt_stories import entry

LOGGER = logging.getLogger(__name__)

#############
# Main Call #
#############
@click.group()
def cli_entry():
    """Main Entrypoint"""
    pass

@cli_entry.command()
@click.option(
    "--story-prompt",
    help="The primary concept of your story to build.",
    type=str,
    default=""
)
@click.option(
    "--n-parts",
    help="The number of parts to the story. Parts have chapters.",
    type=str,
    default=2
)
@click.option(
    "--n-chapters",
    help="The number of chapters to each part. Chapters have sections.",
    type=str,
    default=2
)
@click.option(
    "--n-sec-per-chap",
    help=("The number of sections per chapter. Sectoins are individual"
       "prompts to GPT"),
    type=str,
    default=3
)
def entry(story_prompt, n_parts, n_chapters, n_sec_per_chap):
    """
    Main entrypoint for our story generator.
    """
    args = {
        "story_prompt": story_prompt,
        "n_parts": n_parts,
        "n_chapters": n_chapters,
        "n_sec_per_chap": n_sec_per_chap,
    }

    entry(args)


#########
# CLI Collection #
#########
cli = click.CommandCollection(
    sources = [
        cli_entry,
    ]
)

####
# CLI Entrypoint #
####
if __name__ == "__main__":
    logging.basicConfig(
        format="[ %(asctime)s.%(msecs)03d - %(levelname)s - %(filename)s:%(lineo)d ] %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    cli()